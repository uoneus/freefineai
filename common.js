// ==================== API Configuration ====================

// Multiple API endpoints for load balancing and failover
// IMPORTANT: Update these endpoints to match your actual backend servers
const API_ENDPOINTS = [
    'https://api.freefineai.com/api',
    'https://cloud.sourcespring.cn/api'
];

const IMAGE_BASE_URLS = [
    'https://api.freefineai.com',
    'https://cloud.sourcespring.cn'
];

// API endpoint selection strategy
const API_STRATEGY = {
    RANDOM: 'random',           // Random selection
    ROUND_ROBIN: 'round_robin', // Sequential rotation
    FAILOVER: 'failover',       // Try next on failure
    FASTEST: 'fastest'          // Use fastest responding endpoint
};

// Current strategy (can be changed)
let currentStrategy = API_STRATEGY.RANDOM;

// Round-robin counter
let roundRobinIndex = 0;

// Endpoint health tracking
const endpointHealth = {};
API_ENDPOINTS.forEach(endpoint => {
    endpointHealth[endpoint] = {
        failures: 0,
        lastFailure: null,
        avgResponseTime: null,
        isHealthy: true
    };
});

// ==================== API Endpoint Selection ====================

/**
 * Get an API endpoint based on current strategy
 */
function getAPIEndpoint() {
    const healthyEndpoints = API_ENDPOINTS.filter(endpoint => 
        endpointHealth[endpoint].isHealthy
    );

    // If no healthy endpoints, use all endpoints
    const availableEndpoints = healthyEndpoints.length > 0 ? healthyEndpoints : API_ENDPOINTS;

    switch (currentStrategy) {
        case API_STRATEGY.RANDOM:
            return availableEndpoints[Math.floor(Math.random() * availableEndpoints.length)];
        
        case API_STRATEGY.ROUND_ROBIN:
            const endpoint = availableEndpoints[roundRobinIndex % availableEndpoints.length];
            roundRobinIndex++;
            return endpoint;
        
        case API_STRATEGY.FASTEST:
            // Sort by average response time
            const sorted = [...availableEndpoints].sort((a, b) => {
                const timeA = endpointHealth[a].avgResponseTime || Infinity;
                const timeB = endpointHealth[b].avgResponseTime || Infinity;
                return timeA - timeB;
            });
            return sorted[0];
        
        case API_STRATEGY.FAILOVER:
        default:
            return availableEndpoints[0];
    }
}

/**
 * Get image base URL corresponding to API endpoint
 */
function getImageBaseURL(apiEndpoint) {
    const index = API_ENDPOINTS.indexOf(apiEndpoint);
    return index >= 0 && index < IMAGE_BASE_URLS.length 
        ? IMAGE_BASE_URLS[index] 
        : IMAGE_BASE_URLS[0];
}

/**
 * Mark endpoint as failed
 */
function markEndpointFailed(endpoint) {
    if (endpointHealth[endpoint]) {
        endpointHealth[endpoint].failures++;
        endpointHealth[endpoint].lastFailure = Date.now();
        
        // Mark as unhealthy after 3 consecutive failures
        if (endpointHealth[endpoint].failures >= 3) {
            endpointHealth[endpoint].isHealthy = false;
            console.warn(`[API] Endpoint marked unhealthy: ${endpoint}`);
            
            // Auto-recover after 5 minutes
            setTimeout(() => {
                endpointHealth[endpoint].failures = 0;
                endpointHealth[endpoint].isHealthy = true;
                console.log(`[API] Endpoint recovered: ${endpoint}`);
            }, 5 * 60 * 1000);
        }
    }
}

/**
 * Mark endpoint as successful and update response time
 */
function markEndpointSuccess(endpoint, responseTime) {
    if (endpointHealth[endpoint]) {
        endpointHealth[endpoint].failures = 0;
        endpointHealth[endpoint].isHealthy = true;
        
        // Update average response time (exponential moving average)
        const current = endpointHealth[endpoint].avgResponseTime;
        if (current === null) {
            endpointHealth[endpoint].avgResponseTime = responseTime;
        } else {
            endpointHealth[endpoint].avgResponseTime = current * 0.7 + responseTime * 0.3;
        }
    }
}

// ==================== Enhanced Fetch with Retry ====================

/**
 * Enhanced fetch with automatic retry and failover
 * @param {string} path - API path (e.g., '/v1/generate')
 * @param {object} options - Fetch options
 * @param {number} maxRetries - Maximum retry attempts
 * @returns {Promise<Response>}
 */
async function apiFetch(path, options = {}, maxRetries = 3) {
    let lastError = null;
    const triedEndpoints = new Set();

    for (let attempt = 0; attempt < maxRetries; attempt++) {
        // Get an endpoint that hasn't been tried yet
        let endpoint;
        let attempts = 0;
        do {
            endpoint = getAPIEndpoint();
            attempts++;
        } while (triedEndpoints.has(endpoint) && attempts < API_ENDPOINTS.length * 2);
        
        triedEndpoints.add(endpoint);
        const url = endpoint + path;
        const startTime = Date.now();

        try {
            console.log(`[API] Attempt ${attempt + 1}/${maxRetries}: ${url}`);
            
            const response = await fetch(url, {
                ...options,
                headers: {
                    ...options.headers
                }
            });

            const responseTime = Date.now() - startTime;
            
            // Mark as successful if response is ok
            if (response.ok) {
                markEndpointSuccess(endpoint, responseTime);
                console.log(`[API] Success: ${url} (${responseTime}ms)`);
                
                // Attach metadata to response
                response._apiEndpoint = endpoint;
                response._responseTime = responseTime;
                return response;
            }

            // If response is not ok but not a network error, don't retry
            if (response.status >= 400 && response.status < 500) {
                console.warn(`[API] Client error ${response.status}: ${url}`);
                return response;
            }

            // Server error, mark as failed and retry
            markEndpointFailed(endpoint);
            lastError = new Error(`HTTP ${response.status}: ${response.statusText}`);
            console.warn(`[API] Server error, will retry: ${lastError.message}`);

        } catch (error) {
            markEndpointFailed(endpoint);
            lastError = error;
            console.error(`[API] Network error: ${error.message}`);
        }

        // Wait before retry (exponential backoff)
        if (attempt < maxRetries - 1) {
            const delay = Math.min(1000 * Math.pow(2, attempt), 5000);
            console.log(`[API] Waiting ${delay}ms before retry...`);
            await new Promise(resolve => setTimeout(resolve, delay));
        }
    }

    // All retries failed
    console.error(`[API] All attempts failed after ${maxRetries} retries`);
    throw lastError || new Error('All API endpoints failed');
}

/**
 * Convenience method for GET requests
 */
async function apiGet(path, options = {}) {
    // Merge headers properly
    const headers = {
        ...(options.headers || {})
    };
    
    return apiFetch(path, { 
        ...options, 
        method: 'GET',
        headers: headers
    });
}

/**
 * Convenience method for POST requests
 */
async function apiPost(path, data, options = {}) {
    // Merge headers properly
    const headers = {
        'Content-Type': 'application/json',
        ...(options.headers || {})
    };
    
    return apiFetch(path, {
        ...options,
        method: 'POST',
        headers: headers,
        body: JSON.stringify(data)
    });
}

/**
 * Convenience method for DELETE requests
 */
async function apiDelete(path, options = {}) {
    return apiFetch(path, { ...options, method: 'DELETE' });
}

// ==================== Endpoint Health Check ====================

/**
 * Check health of all endpoints
 */
async function checkEndpointHealth() {
    console.log('[API] Checking endpoint health...');
    
    const checks = API_ENDPOINTS.map(async endpoint => {
        const startTime = Date.now();
        try {
            const response = await fetch(endpoint + '/v1/health', {
                method: 'GET',
                signal: AbortSignal.timeout(5000) // 5 second timeout
            });
            
            const responseTime = Date.now() - startTime;
            
            if (response.ok) {
                markEndpointSuccess(endpoint, responseTime);
                console.log(`[API] ✓ ${endpoint} - ${responseTime}ms`);
                return { endpoint, healthy: true, responseTime };
            } else {
                markEndpointFailed(endpoint);
                console.warn(`[API] ✗ ${endpoint} - HTTP ${response.status}`);
                return { endpoint, healthy: false, error: `HTTP ${response.status}` };
            }
        } catch (error) {
            markEndpointFailed(endpoint);
            console.error(`[API] ✗ ${endpoint} - ${error.message}`);
            return { endpoint, healthy: false, error: error.message };
        }
    });

    const results = await Promise.all(checks);
    return results;
}

// ==================== Exports ====================

// Expose window.API immediately (not inside DOMContentLoaded) so HTML scripts
// that run synchronously can call window.API.getEndpoint() right away.
if (typeof window !== 'undefined') {
    window.API = {
        fetch: apiFetch,
        get: apiGet,
        post: apiPost,
        delete: apiDelete,
        getEndpoint: getAPIEndpoint,
        getImageBaseURL: getImageBaseURL,
        checkHealth: checkEndpointHealth,
        setStrategy: (strategy) => {
            if (Object.values(API_STRATEGY).includes(strategy)) {
                currentStrategy = strategy;
                console.log(`[API] Strategy changed to: ${strategy}`);
            }
        },
        getHealth: () => ({ ...endpointHealth }),
        STRATEGY: API_STRATEGY
    };
}

// ==================== Initialization ====================

// Health checks are disabled by default to avoid marking endpoints as unhealthy
// when the /v1/health route doesn't exist on the backend.
// To enable: window.API.checkHealth() or uncomment below.
//
// if (typeof window !== 'undefined') {
//     window.addEventListener('DOMContentLoaded', () => {
//         checkEndpointHealth();
//         setInterval(checkEndpointHealth, 5 * 60 * 1000);
//     });
// }

// ==================== Legacy Compatibility ====================

// For backward compatibility with existing code
// Note: These are defined in each HTML file to avoid conflicts
// const API_BASE_URL = getAPIEndpoint();
// const IMAGE_BASE_URL = getImageBaseURL(API_BASE_URL);

// ── Shared Navbar Loader ──────────────────────────────────────
function loadNavbar(onLoaded) {
    const placeholder = document.getElementById('navbar-placeholder');
    if (!placeholder) { if (onLoaded) onLoaded(); return; }
    fetch('/navbar.html')
        .then(r => r.text())
        .then(html => {
            // Use a Range to parse and insert HTML with scripts executing properly
            const range = document.createRange();
            range.selectNode(document.body);
            const fragment = range.createContextualFragment(html);
            placeholder.replaceWith(fragment);
            if (onLoaded) onLoaded();
        })
        .catch(function(err) {
            console.warn('Navbar load failed:', err);
            if (onLoaded) onLoaded();
        });
}
