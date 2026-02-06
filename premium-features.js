// Premium Features for FreeFineAI
// Social Share + Unlock Rewards

class PremiumFeatures {
    constructor() {
        this.config = window.SITE_CONFIG || {};
        this.init();
    }
    
    init() {
        this.initSocialShare();
        this.initEmailPopup();
        this.initTrending();
        this.initLiveStats();
        this.initMembership();
    }
    
    // Social Share Feature
    initSocialShare() {
        if (!this.config.ENABLE_SOCIAL_SHARE) return;
        
        // Add share buttons to each image card
        document.addEventListener('DOMContentLoaded', () => {
            this.addShareButtons();
        });
    }
    
    addShareButtons() {
        const imageCards = document.querySelectorAll('[data-image-card]');
        imageCards.forEach(card => {
            const imageName = card.getAttribute('data-image');
            const shareBtn = document.createElement('button');
            shareBtn.innerHTML = '📤';
            shareBtn.className = 'share-btn bg-zinc-800 text-white px-3 py-2 rounded-xl hover:bg-green-600 transition-all';
            shareBtn.onclick = () => this.shareImage(imageName);
            
            const buttonContainer = card.querySelector('.button-container');
            if (buttonContainer) {
                buttonContainer.appendChild(shareBtn);
            }
        });
    }
    
    shareImage(imageName) {
        const imageUrl = `${window.location.origin}/images/${imageName}`;
        const text = `Check out this amazing AI art from FreeFineAI! 🎨`;
        const hashtags = 'AIArt,FluxAI,FreeFineAI';
        
        // Twitter share
        const twitterUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(imageUrl)}&hashtags=${hashtags}`;
        
        // Open share window
        window.open(twitterUrl, 'share', 'width=600,height=400');
        
        // Track share
        this.trackShare(imageName);
        
        // Unlock reward after 2 seconds
        setTimeout(() => {
            this.unlockReward(imageName);
        }, 2000);
    }
    
    trackShare(imageName) {
        const shares = JSON.parse(localStorage.getItem('shared_images') || '[]');
        if (!shares.includes(imageName)) {
            shares.push(imageName);
            localStorage.setItem('shared_images', JSON.stringify(shares));
        }
        
        // Update trending
        this.updateTrendingStats(imageName, 'share');
    }
    
    unlockReward(imageName) {
        showNotification('🎉 Reward Unlocked!', 'High-res version now available for download');
        
        // Mark as unlocked
        const unlocked = JSON.parse(localStorage.getItem('unlocked_images') || '[]');
        if (!unlocked.includes(imageName)) {
            unlocked.push(imageName);
            localStorage.setItem('unlocked_images', JSON.stringify(unlocked));
        }
        
        // Add achievement
        if (window.userProgress) {
            if (!window.userProgress.data.achievements.includes('social_sharer')) {
                window.userProgress.data.achievements.push('social_sharer');
                window.userProgress.save();
                showNotification('🏆 Achievement', 'Social Sharer - Share your first image!');
            }
        }
    }
    
    // Email Popup Feature
    initEmailPopup() {
        if (!this.config.ENABLE_EMAIL_POPUP) return;
        
        const delay = 30000; // 30 seconds
        const hasSubscribed = localStorage.getItem('email_subscribed');
        const lastShown = localStorage.getItem('email_popup_last_shown');
        const now = Date.now();
        
        // Don't show if already subscribed or shown in last 24 hours
        if (hasSubscribed || (lastShown && now - lastShown < 86400000)) {
            return;
        }
        
        setTimeout(() => {
            this.showEmailPopup();
        }, delay);
    }
    
    showEmailPopup() {
        const popup = document.createElement('div');
        popup.id = 'emailPopup';
        popup.className = 'fixed inset-0 bg-black/80 z-[9999] flex items-center justify-center p-4';
        popup.innerHTML = `
            <div class="bg-zinc-900 p-8 rounded-3xl max-w-md w-full border border-white/10 relative animate-fade-in">
                <button onclick="closeEmailPopup()" class="absolute top-4 right-4 text-zinc-400 hover:text-white text-2xl">&times;</button>
                
                <div class="text-center mb-6">
                    <div class="text-5xl mb-4">🎨</div>
                    <h3 class="text-2xl font-black text-white mb-2">
                        Get Weekly AI Art Inspiration
                    </h3>
                    <p class="text-zinc-400 text-sm">
                        Join 10,000+ creators receiving exclusive prompts, tips, and early access to new features
                    </p>
                </div>
                
                <form id="emailForm" class="space-y-4">
                    <input type="email" id="emailInput" placeholder="your@email.com" required
                           class="w-full bg-black/40 border border-white/5 rounded-xl p-4 text-white outline-none focus:border-cyan-500/50 transition">
                    
                    <button type="submit" class="w-full bg-gradient-to-r from-cyan-500 to-blue-500 text-white font-black py-4 rounded-xl hover:from-cyan-400 hover:to-blue-400 transition uppercase tracking-widest">
                        Subscribe Now
                    </button>
                    
                    <p class="text-zinc-600 text-xs text-center">
                        No spam. Unsubscribe anytime. 🔒
                    </p>
                </form>
                
                <div class="mt-6 flex items-center justify-center gap-4 text-xs text-zinc-500">
                    <div class="flex items-center gap-1">
                        <span>✓</span> Weekly Tips
                    </div>
                    <div class="flex items-center gap-1">
                        <span>✓</span> Exclusive Prompts
                    </div>
                    <div class="flex items-center gap-1">
                        <span>✓</span> Early Access
                    </div>
                </div>
            </div>
        `;
        
        document.body.appendChild(popup);
        
        // Handle form submission
        document.getElementById('emailForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleEmailSubmit();
        });
        
        // Track popup shown
        localStorage.setItem('email_popup_last_shown', Date.now());
    }
    
    handleEmailSubmit() {
        const email = document.getElementById('emailInput').value;
        
        // Save to localStorage (in production, send to backend/Mailchimp)
        localStorage.setItem('user_email', email);
        localStorage.setItem('email_subscribed', 'true');
        
        // Close popup
        closeEmailPopup();
        
        // Show success notification
        showNotification('🎉 Welcome!', 'Check your email for a special gift');
        
        // Add achievement
        if (window.userProgress) {
            if (!window.userProgress.data.achievements.includes('newsletter_subscriber')) {
                window.userProgress.data.achievements.push('newsletter_subscriber');
                window.userProgress.save();
            }
        }
        
        // In production, send to backend
        // fetch('/api/subscribe', { method: 'POST', body: JSON.stringify({ email }) });
    }
    
    // Trending Feature
    initTrending() {
        if (!this.config.ENABLE_TRENDING) return;
        
        document.addEventListener('DOMContentLoaded', () => {
            this.displayTrending();
        });
    }
    
    updateTrendingStats(imageName, action) {
        const stats = JSON.parse(localStorage.getItem('trending_stats') || '{}');
        
        if (!stats[imageName]) {
            stats[imageName] = { views: 0, downloads: 0, shares: 0, favorites: 0 };
        }
        
        stats[imageName][action] = (stats[imageName][action] || 0) + 1;
        stats[imageName].score = (stats[imageName].downloads * 3) + 
                                  (stats[imageName].shares * 5) + 
                                  (stats[imageName].favorites * 2) + 
                                  (stats[imageName].views * 1);
        
        localStorage.setItem('trending_stats', JSON.stringify(stats));
    }
    
    displayTrending() {
        const stats = JSON.parse(localStorage.getItem('trending_stats') || '{}');
        const sorted = Object.entries(stats)
            .sort((a, b) => (b[1].score || 0) - (a[1].score || 0))
            .slice(0, 5);
        
        if (sorted.length === 0) return;
        
        const trendingWidget = document.createElement('div');
        trendingWidget.className = 'fixed right-8 top-32 w-64 bg-zinc-900/90 backdrop-blur-md border border-white/10 p-6 rounded-3xl shadow-2xl z-40 hidden lg:block';
        trendingWidget.innerHTML = `
            <div class="flex items-center gap-2 mb-4">
                <span class="text-2xl">🔥</span>
                <h3 class="text-white font-black text-sm uppercase tracking-wider">Trending Now</h3>
            </div>
            <div class="space-y-3">
                ${sorted.map((item, index) => `
                    <div class="flex items-center gap-3 p-2 rounded-xl hover:bg-white/5 transition cursor-pointer">
                        <span class="text-cyan-400 font-black text-sm w-6">#${index + 1}</span>
                        <img src="images/${item[0]}" class="w-12 h-12 rounded-lg object-cover">
                        <div class="flex-1 min-w-0">
                            <div class="text-white text-xs font-bold truncate">${item[0].split('.')[0].replace(/_/g, ' ')}</div>
                            <div class="text-zinc-500 text-[10px]">${item[1].downloads || 0} downloads</div>
                        </div>
                    </div>
                `).join('')}
            </div>
        `;
        
        document.body.appendChild(trendingWidget);
    }
    
    // Live Stats Feature
    initLiveStats() {
        if (!this.config.ENABLE_LIVE_STATS) return;
        
        document.addEventListener('DOMContentLoaded', () => {
            this.displayLiveStats();
            this.updateLiveStats();
        });
    }
    
    displayLiveStats() {
        const statsBar = document.createElement('div');
        statsBar.className = 'fixed bottom-0 left-0 right-0 bg-zinc-900/90 backdrop-blur-md border-t border-white/5 py-3 px-8 z-40';
        statsBar.innerHTML = `
            <div class="max-w-[1400px] mx-auto flex items-center justify-between text-xs">
                <div class="flex items-center gap-6">
                    <div class="flex items-center gap-2">
                        <span class="w-2 h-2 bg-green-500 rounded-full animate-pulse"></span>
                        <span class="text-zinc-400">Online:</span>
                        <span class="text-white font-bold" id="onlineCount">127</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-zinc-400">📥 Total Downloads:</span>
                        <span class="text-cyan-400 font-bold" id="totalDownloads">52,341</span>
                    </div>
                    <div class="flex items-center gap-2">
                        <span class="text-zinc-400">🎨 Images:</span>
                        <span class="text-purple-400 font-bold" id="totalImages">1,247</span>
                    </div>
                </div>
                <div class="text-zinc-500 text-[10px]">
                    Updated in real-time
                </div>
            </div>
        `;
        
        document.body.appendChild(statsBar);
    }
    
    updateLiveStats() {
        setInterval(() => {
            // Simulate real-time updates (in production, fetch from backend)
            const onlineCount = document.getElementById('onlineCount');
            const totalDownloads = document.getElementById('totalDownloads');
            
            if (onlineCount) {
                const current = parseInt(onlineCount.textContent);
                const change = Math.floor(Math.random() * 10) - 5;
                onlineCount.textContent = Math.max(50, current + change);
            }
            
            if (totalDownloads) {
                const current = parseInt(totalDownloads.textContent.replace(/,/g, ''));
                const newCount = current + Math.floor(Math.random() * 3);
                totalDownloads.textContent = newCount.toLocaleString();
            }
        }, 5000);
    }
    
    // Membership Feature
    initMembership() {
        if (!this.config.ENABLE_MEMBERSHIP) return;
        
        document.addEventListener('DOMContentLoaded', () => {
            this.addMembershipBadge();
        });
    }
    
    addMembershipBadge() {
        const tier = localStorage.getItem('membership_tier') || 'free';
        const badges = {
            free: { icon: '🆓', color: 'zinc', name: 'Free' },
            silver: { icon: '🥈', color: 'gray', name: 'Silver' },
            gold: { icon: '🥇', color: 'yellow', name: 'Gold' },
            platinum: { icon: '💎', color: 'cyan', name: 'Platinum' }
        };
        
        const badge = badges[tier];
        const userStats = document.getElementById('userStats');
        
        if (userStats && tier !== 'free') {
            const memberBadge = document.createElement('div');
            memberBadge.className = `flex items-center gap-1 px-2 py-1 bg-${badge.color}-500/20 rounded-full`;
            memberBadge.innerHTML = `
                <span>${badge.icon}</span>
                <span class="text-${badge.color}-400 text-[10px] font-bold uppercase">${badge.name}</span>
            `;
            userStats.parentElement.appendChild(memberBadge);
        }
    }
}

// Global functions
function closeEmailPopup() {
    const popup = document.getElementById('emailPopup');
    if (popup) {
        popup.remove();
    }
}

// Initialize premium features
const premiumFeatures = new PremiumFeatures();

// Export for use in other scripts
window.premiumFeatures = premiumFeatures;
