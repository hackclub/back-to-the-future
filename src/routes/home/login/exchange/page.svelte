<!-- <script lang='ts'>
	import back from "$lib/assets/w8back.png";
	import win8spinner from "$lib/assets/win8spinner.gif"
	import {PUBLIC_HC_CLIENT_ID, PUBLIC_BE_URL} from "$env/static/public"
	import {goto} from "$app/navigation"
	import {onMount} from "svelte"

	function url(): string {
		let item = `https://auth.hackclub.com/oauth/authorize?client_id=${PUBLIC_HC_CLIENT_ID}&redirect_uri=${window.location.href}&response_type=code&scope=${"profile email name slack_id verification_status"}`
		window.location.href = item;
	}

	let error = $state();
	async function handleAuth() {
		// check for code first
		const code = new URLSearchParams(window.location.search).get("code");
		if (!code) {
			error = "Hack Club didn't return a code. This may be because you did not authorise the app, or another error. Please try again later."
			return;
		}

		let res = await fetch(`${PUBLIC_BE_URL}/token?code=${code}&redirect_uri=${window.location.href}`)
		if (!res.ok) {
			error = "There was an internal server error. Please try later, or contact help for more information."
			console.error("response to server failed:", res, await res.json())
			return;
		}

		let data = await res.json();
		if (!data.access_token) {
			error = "The server did not send a valid response. Please try later, or contact help for more information."
			return;
		}

		localStorage.setItem('auth_token', data.access_token);

		goto("/home");
	}

	onMount(() => handleAuth());
</script>

<div class="w-screen h-screen bg-[rgb(17,0,48)] flex items-center justify-center">
	
	<div class="w-full p-10 bg-[rgb(40,0,109)] text-white font-thin flex flex-col justify-center gap-4 shadow-2xl" style="font-family: 'Segoe UI', sans-serif;">
		<div class="flex flex-row items-center gap-4">
			<a href="/"><img src={back} class="invert w-8 h-8 active:bg-black rounded-full"></a>
			<div class="text-3xl mb-1">Sign in to your Hack Club Account</div>
		</div>
		<div class='pl-12'>
			Signing into your Hack Club account allows you to join this YSWS. 
		</div>
		<div class="pl-12 flex flex-row gap-4 items-center">
			<button onclick={url} disabled={!!!error} class="inline-block bg-[rgb(83,0,188)] text-white disabled:text-gray-400 border-3 border-white disabled:border-gray-400 font-semibold px-4 py-1.5 not-disabled:active:bg-white active:text-black transition-colors duration-75 uppercase text-left tracking-wide">
	  			Sign in with Hack Club
			</button>
			{#if !!!error}
			<img src={win8spinner} class="invert w-8 h-8">
			{/if}
		</div>
		<div class='pl-12 text-yellow-400'>
			{error}
		</div>
	</div>

</div> -->