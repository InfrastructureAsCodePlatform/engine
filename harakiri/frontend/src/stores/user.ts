// @ts-check
import { defineStore, acceptHMRUpdate } from 'pinia'

async function apiLogin(email: string, password: string) {
    // @ts-ignore
    const res = await fetch(`/auth/token/`, {
        method: 'POST',
        mode: 'cors',
        body: JSON.stringify({ email, password }),
        headers: {
            'Content-Type': 'application/json',
        }
    });
    const data = await res.json();

    if (!data) {
        return Promise.reject(new Error('invalid credentials'));
    }

    return data;
}

export const useUserStore = defineStore({
    id: 'user',
    state: () => ({
        email: '',
        loggedIn: false,
    }),

    actions: {
        logout() {
            console.info('Logged out');

            this.$patch({
                email: '',
                loggedIn: false,
            });
        },

        async login(email: string, password: string) {
            if (this.loggedIn) {
                return;
            }

            try {
                const userData = await apiLogin(email, password);

                this.$patch({
                    email: email,
                    loggedIn: true,
                    ...userData,
                });
            } catch (e) {
                console.error(e);
            }
        },
    },
})

if (import.meta.hot) {
    import.meta.hot.accept(acceptHMRUpdate(useUserStore, import.meta.hot))
}
