import type { PageLoad } from './$types';
import {redirect} from "@sveltejs/kit"

export const load: PageLoad = ({ }) => {
	if (typeof window === 'undefined') return;
	throw redirect(308, "/");

    const hasToken = !!localStorage.getItem('auth_token');
    if (!hasToken) {
        throw redirect(303, '/home/login');
    }
}