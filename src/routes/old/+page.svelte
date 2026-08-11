<script lang="ts">
	import { onMount, tick } from 'svelte';
	import { cubicInOut } from 'svelte/easing';
	import { fade, fly } from 'svelte/transition';
	import { slide } from 'svelte/transition';
	import Marqueeck from '@arisbh/marqueeck';

	// Generate random coordinates for stars
	let smallStars = Array.from({ length: 150 }, () => ({
		x: Math.random() * 100,
		y: Math.random() * 100
	}));
	let bigStars = Array.from({ length: 50 }, () => ({
		x: Math.random() * 100,
		y: Math.random() * 100
	}));

	let mouseX = $state(0);
	let mouseY = $state(0);
	let timeOffset = $state(0);
	let targetMouseX = 0;
	let targetMouseY = 0;
	let showText = $state(false);

	onMount(() => {
		let frame: number;
		let lastTime = performance.now();

		const loop = (time: number) => {
			const delta = time - lastTime;
			lastTime = time;
			timeOffset += delta * 0.003; // Base upward speed

			// Smooth inertia for mouse movement
			mouseX += (targetMouseX - mouseX) * 0.05 * (delta / 16);
			mouseY += (targetMouseY - mouseY) * 0.05 * (delta / 16);

			frame = requestAnimationFrame(loop);
		};

		frame = requestAnimationFrame(loop);

		const timer = setTimeout(() => {
			showText = true;
		}, 1500);

		return () => {
			cancelAnimationFrame(frame);
			clearTimeout(timer);
		};
	});

	// Track mouse position for parallax effect
	function handleMouseMove(e: MouseEvent) {
		targetMouseX = (e.clientX / window.innerWidth - 0.5) * 2;
		targetMouseY = (e.clientY / window.innerHeight - 0.5) * 2;
	}

	const shopItems = [
		{
			name: 'Ancient VR Headset',
			image: '/ancient-vr-headset.jpeg',
			description: 'I mean technically Quest 1 is old enough to count here???'
		},
		{
			name: 'Old android wear',
			image: '/lg-g-watch.jpg.webp',
			description: 'Anything but playing minecraft on your wrist.'
		},
		{
			name: 'Old Windows Phone',
			image: '/old-windowsphone.jpg',
			description: 'A relic back to the days when Microsoft had soul and an actual product.'
		},
		{
			name: 'Old MacBook',
			image: '/old-macbook.jpg',
			description:
				'Features the legendary glowing Apple logo, will repel Thinkpad users within 2 miles.'
		},
		{
			name: 'Old iPhone',
			image: '/old-iphone.jpg',
			description: 'Pros: jelbrek, cons: wen eta updete.'
		},
		{
			name: 'Old ThinkPad',
			image: '/old-thinkpad.jpg',
			description:
				'Features the legendary glowing red dot, will repel MacBook users within 2 miles.'
		},
		{
			name: 'Platform API Key',
			image: '/platform-api-key.png',
			description:
				'Power the tweaks you made with more than 2 requests of data. Your choice as long as your app uses it.'
		},
		{
			name: 'Spinning Rust HDD',
			image: '/hard-drive.jpg',
			description: 'I threw this in here just in case you wanted storage.'
		},
		{
			name: 'and more???',
			image: '',
			description:
				'yes!!! and more (such as other old stuff, and stuff that might be useful for your journey, requests are open!).'
		}
	];

	const faqs = [
		{
			question: 'When will this start?',
			answer: 'Well into the future, hoping that you guys show interest!!!!'
		},
		{
			question: 'How can I track my progress?',
			answer:
				'You will be using a combination of Hackatime and Lapse to track time spent researching and coding. You have to be between 13-18yo.'
		},
		{
			question: 'Can I work on new software on a new device?',
			answer: 'No, the goal is to work on software targeting an old device.'
		},
		{
			question: 'Will the shop be expanded?',
			answer: 'Absolutely! Join the Slack channel to suggest items you want to see in the shop.'
		},
		{
			question: 'Can I help out?',
			answer:
				'Yes! DM @atomtables to find out how you can help out, whether that be through coding, design, or just spreading the word.'
		},
		{
			question: "I don't understand. Who do I ask for help?",
			answer: 'DM @atomtables and ask away! Slack channel coming soon'
		}
	];
</script>

<svelte:window on:mousemove={handleMouseMove} />

<div class="fixed -z-10 h-screen w-full overflow-hidden bg-slate-100 dark:bg-slate-950">
	<div
		class="absolute inset-x-[-5%] inset-y-[-5%] h-[110%] w-[110%] will-change-transform"
		style="transform: translate({mouseX * -10}px, {mouseY * -10}px)"
	>
		{#each smallStars as star}
			<div
				class="absolute rounded-full bg-black opacity-40 dark:bg-white"
				style="left: {star.x}%; top: {(((star.y - timeOffset) % 100) + 100) %
					100}%; width: 2px; height: 2px;"
			></div>
		{/each}
	</div>

	<div
		class="absolute inset-x-[-10%] inset-y-[-10%] h-[120%] w-[120%] will-change-transform"
		style="transform: translate({mouseX * -30}px, {mouseY * -30}px)"
	>
		{#each bigStars as star}
			<div
				class="absolute rounded-full bg-black opacity-90 dark:bg-white"
				style="left: {star.x}%; top: {(((star.y - timeOffset * 2.5) % 100) + 100) %
					100}%; width: 4px; height: 4px; box-shadow: 0 0 6px rgba(255,255,255,0.6);"
			></div>
		{/each}
	</div>
</div>

<div class="relative flex h-screen w-full items-center justify-center overflow-hidden">
	<div
		class="relative mx-auto flex w-full max-w-5xl flex-col items-center justify-center lg:flex-row"
	>
		<div
			class="relative z-10 flex h-100 w-125 shrink-0 items-center justify-center"
			style="perspective: 600px;"
		>
			<div
				class="absolute flex h-full w-full items-center justify-center"
				style="transform: translate({mouseX * -15}px, {mouseY * -15}px); will-change: transform;"
			>
				<img src="/mba.png" alt="macbook air" class="macbook absolute w-125" />
			</div>
			<div
				class="absolute flex h-full w-full items-center justify-center"
				style="transform: translate({mouseX * -10}px, {mouseY * -10}px); will-change: transform;"
			>
				<img src="/bb.png" alt="blackberry" class="blackberry absolute bottom-8 left-0 h-48" />
			</div>
			<div
				class="absolute flex h-full w-full items-center justify-center"
				style="transform: translate({mouseX * -5}px, {mouseY * -5}px); will-change: transform;"
			>
				<img src="/watch.png" alt="watch" class="watch absolute right-4 bottom-8 h-36" />
			</div>
		</div>

		{#if showText}
			<div transition:slide={{ axis: 'x', duration: 1200, easing: cubicInOut }}>
				<div
					in:fly={{ x: 40, duration: 1000, delay: 300, easing: cubicInOut }}
					class="z-20 ml-16 flex w-100 flex-col gap-6"
				>
					<h1 class="font-ndot text-6xl font-black">
						BACK TO<br />THE FUTURE
					</h1>
					<p class="text-xl leading-relaxed font-medium text-slate-600 dark:text-slate-300">
						Bring obsolete devices back to the Internet-connected future. Get cool stuff to make
						yourself modern.
					</p>
				</div>
			</div>
		{/if}
	</div>

	<div
		class="animate-bounceopacity-60 absolute bottom-8 left-1/2 flex -translate-x-1/2 transform flex-col items-center"
	>
		<svg
			xmlns="http://www.w3.org/2000/svg"
			width="24"
			height="24"
			viewBox="0 0 24 24"
			fill="none"
			stroke="currentColor"
			stroke-width="2"
			stroke-linecap="round"
			stroke-linejoin="round"
		>
			<path d="M12 5v14M19 12l-7 7-7-7" />
		</svg>
	</div>
</div>

<div class="w-full bg-slate-200/20 p-10 backdrop-blur-sm dark:bg-slate-800/20">
	<div class="m-auto flex max-w-5xl flex-col gap-10 lg:flex-row">
		<div class="shrink-0">
			<img src="/xp.png" alt="windows xp" class="shadow-lg max-lg:w-full lg:h-96" />
			<div
				class="flex flex-row items-center justify-center rounded-b-full bg-amber-100 p-2 text-black"
			>
				<audio controls class="w-16">
					<source src="/dialup.mp3" type="audio/mpeg" />
					Your browser does not support the audio element.
				</audio>
				<div class="">nostalgia warning: do not press if you are over 25.</div>
			</div>
		</div>
		<div class="flex flex-col gap-4">
			<h2 class="font-ndot text-3xl font-bold">Are you old enough to remember? Probably not...</h2>
			<p class="text-lg leading-relaxed font-medium text-slate-600 dark:text-slate-300">
				If you're between the ages of 13-18, there might be a time in your infancy where you saw a
				computer from the '00s actually connect to the Internet.
				<br /><br />
				If you miss that, then this You-Ship-We-Ship is for YOU!!! Yes you, that one person who's been
				<b>looking for a reason to mess around with that ancient laptop</b> in the attic! And you
				over there who wants to try to do something with a <b>phone from before you were born</b>!
				and ESPECIALLY you, that person who wants to save a
				<b>piece of history from the landfill, or worse, ebay...</b>
			</p>
		</div>
	</div>
</div>

<div class="w-full bg-slate-300/30 p-10 backdrop-blur-sm dark:bg-slate-700/30">
	<div class="m-auto flex max-w-5xl flex-col gap-10">
		<div class="flex flex-col gap-4">
			<h2 class="font-ndot text-3xl font-bold">
				Wait I don't know what to do??? How does ts (this) work?
			</h2>
			<p class="text-lg leading-relaxed font-medium text-slate-600 dark:text-slate-300">
				Your goal in this project is to restore old software to run on new services. I included some
				cool examples by people in the community below.
			</p>
		</div>
	</div>
	<Marqueeck class="mt-4" options={{ direction: 'left' }}>
		<div
			class="m-2 flex h-64 w-64 items-center justify-center rounded-lg bg-slate-400/50 dark:bg-slate-800/50"
		>
			<div class="text-center">
				<h2 class="font-ndot text-xl font-bold">Aqua Proxy</h2>
				<div class="mt-2 p-1 text-sm">
					A project that helps to fix SSL issues on old versions of OS X, providing an HTTP and IMAP
					proxy that can be used to connect to modern websites, mail servers, use native Twitter
					integrations/apps with BlueSky, and more.
				</div>
				<div>
					<a
						href="https://github.com/wowfunhappy/aquaproxy"
						class="font-ndot57 text-blue-500 hover:underline">Github</a
					>
					<a
						href="https://forums.macrumors.com/threads/aqua-proxy-fix-connection-issues-on-os-x-10-6-10-9.2459969/"
						class="font-ndot57 ml-4 text-blue-500 hover:underline">MacRumors</a
					>
				</div>
			</div>
		</div>
		<div
			class="m-2 flex h-64 w-64 items-center justify-center rounded-lg bg-slate-400/50 dark:bg-slate-800/50"
		>
			<div class="text-center">
				<h2 class="font-ndot text-xl font-bold">DiscOld</h2>
				<div class="mt-2 p-1 text-sm">
					A jailbreak tweak for old versions of iOS that allows you to use the native Discord app on
					iOS 7/8/9 devices as if it were 2016 and you just bought a spiffy new iPhone 5s off the
					used market. (it is kinda old so may not work anymore)
				</div>
				<div>
					<a
						href="https://cydia.invoxiplaygames.uk/package/discold"
						class="font-ndot57 ml-4 text-blue-500 hover:underline">InvoxiPlayGames</a
					>
				</div>
			</div>
		</div>
		<div
			class="m-2 flex h-64 w-64 items-center justify-center rounded-lg bg-slate-400/50 dark:bg-slate-800/50"
		>
			<div class="text-center">
				<h2 class="font-ndot text-xl font-bold">Retrogram</h2>
				<div class="mt-2 p-1 text-sm">
					A custom server implementation AND patched app package that allows you to use the native
					Instagram app on a custom server (hosted by them) on old versions of Windows Phone, iOS,
					and Android, giving the full 2012 experience.
				</div>
				<div>
					<a
						href="http://rgdownload.sfproj.xyz/"
						class="font-ndot57 ml-4 text-blue-500 hover:underline">Sfproj</a
					>
				</div>
			</div>
		</div>
		<div
			class="m-2 flex h-64 w-64 items-center justify-center rounded-lg bg-slate-400/50 dark:bg-slate-800/50"
		>
			<div class="text-center">
				<h2 class="font-ndot text-xl font-bold">Legacy Update</h2>
				<div class="mt-2 p-1 text-sm">
					A tweak to Windows Update on XP, Vista, 7 et al. that allows you to receive the latest
					updates and patches from Microsoft, even if SSL issues or down servers would normally
					prevent you from doing so. (it even gets you embedded drivers!)
				</div>
				<div>
					<a href="https://legacyupdate.net" class="font-ndot57 ml-4 text-blue-500 hover:underline"
						>Legacy Update</a
					>
					<a
						href="https://github.com/LegacyUpdate/LegacyUpdate"
						class="font-ndot57 ml-4 text-blue-500 hover:underline">Github</a
					>
				</div>
			</div>
		</div>
	</Marqueeck>
</div>

<div class="w-full bg-slate-200/30 p-10 backdrop-blur-sm dark:bg-slate-800/30">
	<div class="m-auto flex max-w-5xl flex-col gap-10 lg:flex-row">
		<div class="flex shrink flex-col gap-4">
			<h2 class="font-ndot text-3xl font-bold">But what should I include?</h2>
			<div class="text-lg leading-relaxed font-medium text-slate-600 dark:text-slate-300">
				<span class="font-light"> Make sure you do the following: </span>
				<br />
				<ul class="list-inside list-disc">
					<li>
						Find a program, networked or otherwise, on an <b>old</b> system that no longer works.
						<ul class="ml-8 list-inside list-disc text-sm font-thin">
							<li>
								Try to aim for unique services that don't already exist, or a unique implementation
								that hasn't been seen before.
							</li>
						</ul>
					</li>
					<li>
						Use <b>lapse</b> to track your progress spent on figuring out why it no longer works.
						<ul class="ml-8 list-inside list-disc text-sm font-thin">
							<li>
								You can use tools like <b>Charles</b> or <b>Burpsuite</b> to proxy requests to see what's
								going on.
							</li>
							<li>
								If the app is one that expires on old versions, like WhatsApp Desktop, you can find
								and disable the killswitch.
							</li>
							<li>You should document your findings and what you were able to accomplish.</li>
						</ul>
					</li>
					<li>
						Use <b>hackatime</b> to track your progress engineering a fix, a patch, or a workaround
						to make it work again.
						<ul class="ml-8 list-inside list-disc text-sm font-thin">
							<li>
								You should try to package your app, tweak, or patch to make it easily installable on
								"new" systems.
							</li>
							<li>
								Make sure you record your progress, as well as your end result, as it may be harder
								for others to replicate.
							</li>
						</ul>
					</li>
					<li>
						Include a good README.md to explain your work, a video demo of your project working.
					</li>
				</ul>
			</div>
		</div>
		<img src="/clippy.png" alt="clippy" class="w-48 shrink-0 object-contain lg:w-72" />
	</div>
</div>

<div class="w-full p-10">
	<div class="m-auto flex max-w-5xl">
		<ul
			class="list-inside list-disc leading-relaxed font-medium text-slate-600 dark:text-slate-300"
		>
			<li>
				Tier 1 projects add back native functionality with no dependency, like logging into IM
				services on the native old client.
			</li>
			<li>
				Tier 2 projects add back native app functionality, but with some sort of external proxy or
				workaround, like using a custom proxy to connect to the old Twitter app. (Proxies
				self-hosted on the system are still Tier 1).
			</li>
			<li>
				Tier 3 projects replace native app functionality with a custom made app by you, like a
				custom made Twitter client for Windows Phone that uses the new API.
			</li>
			<li>
				Depending on a number of factors, such as the quality, uniqueness, tier, and time spent on
				your project, you'll get more rewards on the shop!
			</li>
		</ul>
	</div>
</div>

<div class="w-full bg-slate-300/30 p-10 backdrop-blur-sm dark:bg-slate-700/30">
	<div class="m-auto flex max-w-6xl flex-col gap-10">
		<div class="flex flex-col gap-4 text-center">
			<h2 class="font-ndot text-3xl font-bold">All right, but what's in it for me?</h2>
			<div class="text-lg leading-relaxed font-medium text-slate-600 dark:text-slate-300">
				You get access to this amazing shop!!!
			</div>
		</div>
		<div class="mt-4 flex flex-row flex-wrap justify-center gap-6">
			{#each shopItems as item}
				<div
					class="flex w-full flex-col items-center gap-4 rounded-2xl border border-slate-300/50 bg-slate-100/80 p-5 shadow-xl transition-transform hover:scale-105 hover:shadow-2xl sm:flex-row md:w-[calc(50%-1.5rem)] lg:w-[calc(33%-1.5rem)] dark:border-slate-700/50 dark:bg-slate-900/80"
				>
					<img
						src={item.image}
						alt={item.name}
						class="h-28 w-28 shrink-0 rounded-xl bg-white object-cover shadow-md"
					/>
					<div class="flex flex-col items-center text-center sm:items-start sm:text-left">
						<h3 class="font-ndot mb-1 text-xl font-bold">{item.name}</h3>
						<p class="text-sm font-medium text-slate-500 dark:text-slate-400">{item.description}</p>
					</div>
				</div>
			{/each}
		</div>
	</div>
</div>

<div class="w-full bg-slate-200/30 p-10 backdrop-blur-sm dark:bg-slate-800/30">
	<div class="m-auto flex max-w-4xl flex-col gap-8">
		<h2 class="font-ndot text-center text-3xl font-bold">Frequently Asked Questions</h2>
		<div class="flex flex-col gap-6">
			{#each faqs as faq}
				<div
					class="flex flex-col gap-2 rounded-xl border border-slate-300/50 bg-slate-100/50 p-6 dark:border-slate-700/50 dark:bg-slate-900/50"
				>
					<h3 class="text-xl font-bold text-slate-800 dark:text-slate-200">{faq.question}</h3>
					<p class="text-lg leading-relaxed font-medium text-slate-600 dark:text-slate-400">
						{faq.answer}
					</p>
				</div>
			{/each}
		</div>
	</div>
</div>

<div class="w-full border-t-2 bg-slate-300/30 p-10 backdrop-blur-sm dark:bg-slate-700/30">
	<div class="m-auto flex max-w-6xl flex-col gap-10">
		<div class="flex flex-col gap-4 text-center">
			<h2 class="font-ndot text-3xl font-bold">WHAT AM I WAITING FOR??? PUT ME ON RIGHT NOW!!!</h2>
			<div class="text-lg leading-relaxed font-medium text-slate-600 dark:text-slate-300">
				wait i need the link to join oops
			</div>
			<button
				class="mx-auto mt-4 hover:underline"
				onclick={() => {
					alert(
						"yeaaa... i'm gonna be real i didn't get this far into development. RSVP form coming soon I promise!!!!!!!\n\n\n#NOTIMPL"
					);
				}}
			>
				<a href="#" class="font-ndot57 text-lg">yea lemme join</a>
			</button>
		</div>
	</div>
</div>

<footer
	class="w-full bg-slate-200/30 p-10 text-center text-sm text-slate-500 backdrop-blur-sm dark:bg-slate-800/30 dark:text-slate-400"
>
	brought to you by <b>atomtables</b>
	<br />
	a hack club initiative
</footer>

<style>
	@keyframes float {
		0% {
			transform: rotate3D(1, 0, 0, 60deg);
			scale: 1.4;
			opacity: 0;
		}
		75% {
			opacity: 1;
		}
		100% {
			transform: rotateX(0deg);
			scale: 1;
		}
	}

	@keyframes slideVibrate {
		0% {
			transform: translateX(-100px);
			opacity: 0;
		}
		40% {
			transform: translateX(0);
			opacity: 1;
		}
		50% {
			transform: translateX(0) rotate(-6deg);
		}
		60% {
			transform: translateX(0) rotate(6deg);
		}
		70% {
			transform: translateX(0) rotate(-6deg);
		}
		80% {
			transform: translateX(0) rotate(4deg);
		}
		90% {
			transform: translateX(0) rotate(-2deg);
		}
		100% {
			transform: translateX(0) rotate(0deg);
			opacity: 1;
		}
	}

	@keyframes smoothIn {
		0% {
			transform: scale(0.8) translateY(30px);
			opacity: 0;
		}
		100% {
			transform: scale(1) translateY(0);
			opacity: 1;
		}
	}

	.macbook {
		animation: float 1.5s ease-in-out both;
	}

	.blackberry {
		animation: slideVibrate 1.2s ease-out 0.8s both;
	}

	.watch {
		animation: smoothIn 1s cubic-bezier(0.2, 0.8, 0.2, 1) 1.2s both;
	}

	/* Style for restricting audio controls format (mostly supported on webkit browsers like Chrome/Safari) */
	.custom-audio::-webkit-media-controls-timeline,
	.custom-audio::-webkit-media-controls-current-time-display,
	.custom-audio::-webkit-media-controls-time-remaining-display,
	.custom-audio::-webkit-media-controls-mute-button,
	.custom-audio::-webkit-media-controls-volume-slider {
		display: none !important;
	}

	.custom-audio::-webkit-media-controls-panel {
		justify-content: center;
		background-color: transparent;
	}
</style>
