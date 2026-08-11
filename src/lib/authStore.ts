// src/lib/authStore.ts (Svelte 5 Runes example)
export class AuthState {
    user = $state<{ email: string; name: string } | null>(null);
    token = $state<string | null>(null);
    loading = $state(true);

    constructor() {
        // Run only in browser
        if (typeof window !== 'undefined') {
            this.init();
        }
    }

    private init() {
        const savedToken = localStorage.getItem('auth_token');
        const savedUser = localStorage.getItem('auth_user');
        
        if (savedToken && savedUser) {
            this.token = savedToken;
            this.user = JSON.parse(savedUser);
        }
        this.loading = false;
    }

    login(token: string, user: { email: string; name: string }) {
        this.token = token;
        this.user = user;
        localStorage.setItem('auth_token', token);
        localStorage.setItem('auth_user', JSON.stringify(user));
    }

    logout() {
        this.token = null;
        this.user = null;
        localStorage.removeItem('auth_token');
        localStorage.removeItem('auth_user');
    }
}

export const auth = new AuthState();
