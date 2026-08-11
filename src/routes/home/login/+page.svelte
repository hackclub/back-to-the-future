<script lang='ts'>
	import back from "$lib/assets/w8back.png";
	import {PUBLIC_HC_CLIENT_ID} from "$env/static/public"

	function url(): string {
		let item = `https://auth.hackclub.com/oauth/authorize?client_id=${PUBLIC_HC_CLIENT_ID}&redirect_uri=${window.location.href + "/exchange"}&response_type=code&scope=${"profile email name slack_id verification_status"}`
		window.location.href = item;
	}
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
		<div class="pl-12">
			<button onclick={url} class="inline-block bg-[rgb(83,0,188)] text-white border-3 border-white font-semibold px-4 py-1.5 active:bg-white active:text-black transition-colors duration-75 uppercase text-left tracking-wide">
	  			Sign in with Hack Club
			</button>
		</div>
	</div>

</div>