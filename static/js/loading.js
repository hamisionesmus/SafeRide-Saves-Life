// SafeRide Loading Screen JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Initialize loading sequence
    initializeLoadingScreen();
});

function initializeLoadingScreen() {
    // Start background animations
    startBackgroundAnimation();

    // Start loading progress
    startLoadingProgress();

    // Initialize voiceover and wait for it to complete
    initializeVoiceover();
}

function startBackgroundAnimation() {
    // Background particles are animated via CSS
    // Additional JavaScript animations can be added here if needed
}

function startLoadingProgress() {
    const progressBar = document.querySelector('.loading-progress');
    const loadingText = document.querySelector('.loading-text');

    const loadingSteps = [
        { progress: 20, text: 'Initializing SafeRide...' },
        { progress: 40, text: 'Loading AI models...' },
        { progress: 60, text: 'Setting up offline mode...' },
        { progress: 80, text: 'Preparing hazard detection...' },
        { progress: 100, text: 'Ready to save lives!' }
    ];

    let currentStep = 0;

    const progressInterval = setInterval(() => {
        if (currentStep < loadingSteps.length) {
            const step = loadingSteps[currentStep];
            progressBar.style.width = step.progress + '%';
            loadingText.textContent = step.text;
            currentStep++;
        } else {
            clearInterval(progressInterval);
        }
    }, 800);
}

function initializeVoiceover() {
    const voiceover = document.getElementById('voiceover');

    // Set up audio event listeners first
    if (voiceover) {
        voiceover.addEventListener('ended', () => {
            console.log('Voiceover ended, transitioning to main app...');
            completeLoading();
        });

        voiceover.addEventListener('error', () => {
            console.log('Audio failed, using Web Speech API');
            initializeWebSpeech();
        });

        // Try to load and play audio
        if (voiceover.readyState >= 2) {
            // Audio is loaded and ready
            setTimeout(() => {
                playVoiceover();
            }, 500);
        } else {
            // Wait for audio to load
            voiceover.addEventListener('canplaythrough', () => {
                setTimeout(() => {
                    playVoiceover();
                }, 500);
            });

            // Fallback timeout in case audio never loads
            setTimeout(() => {
                if (!voiceover.played || voiceover.paused) {
                    console.log('Audio load timeout, using Web Speech API');
                    initializeWebSpeech();
                }
            }, 3000);
        }
    } else {
        // No audio element found, use Web Speech API
        initializeWebSpeech();
    }
}

function playVoiceover() {
    const voiceover = document.getElementById('voiceover');
    voiceover.volume = 0.7;
    voiceover.play().catch(error => {
        console.log('Audio playback failed, using Web Speech API');
        initializeWebSpeech();
    });
}

function initializeWebSpeech() {
    // Check if Web Speech API is supported
    if ('speechSynthesis' in window) {
        // Speak immediately when page loads
        console.log('Web Speech API available, starting voiceover...');
        speakWelcomeMessage();

        // Fallback timeout in case speech synthesis fails
        setTimeout(() => {
            console.log('Speech timeout reached, completing loading...');
            completeLoading();
        }, 10000); // 10 seconds fallback
    } else {
        console.log('Web Speech API not supported, using fallback...');
        // No speech support, complete loading after delay
        setTimeout(() => {
            completeLoading();
        }, 3000);
    }
}

function speakWelcomeMessage() {
    const message = "Welcome to SafeRide - Save Life, an offline-first driver assistant powered by OpenAI's GPT-OSS models. In this demonstration, I'll show you how SafeRide provides intelligent, multilingual hazard detection completely offline - no internet required.";

    const utterance = new SpeechSynthesisUtterance(message);

    // Configure voice settings for maximum audibility
    utterance.volume = 1.0;  // Maximum volume
    utterance.rate = 0.8;    // Slightly slower for clarity
    utterance.pitch = 1.0;   // Natural pitch

    // Add visual indicator that voice is speaking
    const voiceIndicator = document.createElement('div');
    voiceIndicator.id = 'voice-indicator';
    voiceIndicator.innerHTML = '🔊 Speaking...';
    voiceIndicator.style.cssText = `
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(0, 0, 0, 0.8);
        color: white;
        padding: 20px 30px;
        border-radius: 15px;
        font-size: 18px;
        font-weight: bold;
        z-index: 10000;
        animation: pulse 1s infinite;
    `;
    document.body.appendChild(voiceIndicator);

    // Add event listener for when speech ends
    utterance.addEventListener('end', () => {
        console.log('Speech ended, transitioning to main app...');
        if (voiceIndicator.parentNode) {
            voiceIndicator.remove();
        }
        completeLoading();
    });

    utterance.addEventListener('start', () => {
        console.log('Speech started...');
    });

    utterance.addEventListener('error', (e) => {
        console.log('Speech error:', e);
        if (voiceIndicator.parentNode) {
            voiceIndicator.remove();
        }
        completeLoading();
    });

    // Try to use the best available voice
    const voices = speechSynthesis.getVoices();
    let selectedVoice = null;

    // Prefer English voices
    selectedVoice = voices.find(voice =>
        voice.lang.startsWith('en') &&
        (voice.name.toLowerCase().includes('female') ||
         voice.name.toLowerCase().includes('woman') ||
         voice.name.toLowerCase().includes('zira') ||
         voice.name.toLowerCase().includes('susan'))
    );

    // If no female English voice, use any English voice
    if (!selectedVoice) {
        selectedVoice = voices.find(voice => voice.lang.startsWith('en'));
    }

    // If no English voice, use any available voice
    if (!selectedVoice && voices.length > 0) {
        selectedVoice = voices[0];
    }

    if (selectedVoice) {
        utterance.voice = selectedVoice;
        console.log('Using voice:', selectedVoice.name, selectedVoice.lang);
    }

    // Speak the message
    try {
        speechSynthesis.speak(utterance);
        console.log('Voiceover started successfully');
    } catch (error) {
        console.log('Speech synthesis failed:', error);
        if (voiceIndicator.parentNode) {
            voiceIndicator.remove();
        }
        completeLoading();
    }
}

function completeLoading() {
    // Add completion animation
    const container = document.querySelector('.loading-container');
    container.style.animation = 'fadeOut 1s ease-out forwards';

    // Redirect to main app after animation
    setTimeout(() => {
        window.location.href = '/app';
    }, 1000);
}

// Add fadeOut animation
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeOut {
        from {
            opacity: 1;
            transform: scale(1);
        }
        to {
            opacity: 0;
            transform: scale(1.1);
        }
    }
`;
document.head.appendChild(style);

// Handle mobile device orientation
function handleOrientationChange() {
    // Adjust layout for mobile devices
    const mobileMockup = document.querySelector('.mobile-mockup');
    if (window.innerWidth < 768) {
        if (mobileMockup) {
            mobileMockup.style.display = 'none';
        }
    }
}

// Listen for orientation changes
window.addEventListener('resize', handleOrientationChange);
window.addEventListener('orientationchange', handleOrientationChange);

// Initialize on load
handleOrientationChange();

// Add interactive elements
document.addEventListener('click', function(e) {
    // Add ripple effect on click
    const ripple = document.createElement('div');
    ripple.style.position = 'absolute';
    ripple.style.borderRadius = '50%';
    ripple.style.background = 'rgba(255, 255, 255, 0.3)';
    ripple.style.width = '20px';
    ripple.style.height = '20px';
    ripple.style.left = e.clientX - 10 + 'px';
    ripple.style.top = e.clientY - 10 + 'px';
    ripple.style.animation = 'ripple 0.6s linear';
    document.body.appendChild(ripple);

    setTimeout(() => {
        ripple.remove();
    }, 600);
});

// Add ripple animation
const rippleStyle = document.createElement('style');
rippleStyle.textContent = `
    @keyframes ripple {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
`;
document.head.appendChild(rippleStyle);

// Performance monitoring
function monitorPerformance() {
    if ('performance' in window) {
        window.addEventListener('load', function() {
            const perfData = performance.getEntriesByType('navigation')[0];
            console.log('Page load time:', perfData.loadEventEnd - perfData.loadEventStart, 'ms');
        });
    }
}

monitorPerformance();