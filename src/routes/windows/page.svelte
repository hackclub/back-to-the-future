<!-- <script lang="ts">
	import readme from '$lib/assets/readme.png';
	import finder from '$lib/assets/finder.png';
	import controlstrip from '$lib/assets/controlstrip.png';
	import win95 from '$lib/assets/win95.png';

	function draggable(node: HTMLElement) {
		let isDragging = false;
		let startX: number, startY: number;
		let startLeft: number, startTop: number;

		function handleMouseDown(e: MouseEvent) {
			// Prevent dragging when clicking inside interactive controls
			const target = e.target as HTMLElement;
			if (target.closest('.no-drag')) return;

			isDragging = true;
			startX = e.clientX;
			startY = e.clientY;

			startLeft = parseInt(node.style.left) || 0;
			startTop = parseInt(node.style.top) || 0;

			window.addEventListener('mousemove', handleMouseMove);
			window.addEventListener('mouseup', handleMouseUp);
		}

		function handleMouseMove(e: MouseEvent) {
			if (!isDragging) return;
			window.getSelection()?.removeAllRanges();

			const dx = e.clientX - startX;
			const dy = e.clientY - startY;

			const parent = node.parentElement;
			if (!parent) return;

			const parentRect = parent.getBoundingClientRect();
			const nodeRect = node.getBoundingClientRect();

			let newLeft = startLeft + dx;
			let newTop = startTop + dy;

			// Restrict bounds (keep top within parent and leave room for taskbar)
			const maxLeft = parentRect.width - nodeRect.width;
			const maxTop = parentRect.height - nodeRect.height - 30; // 30px reserved for Taskbar

			newLeft = Math.max(0, Math.min(newLeft, maxLeft));
			newTop = Math.max(0, Math.min(newTop, maxTop));

			node.style.left = `${newLeft}px`;
			node.style.top = `${newTop}px`;
		}

		function handleMouseUp() {
			isDragging = false;
			window.removeEventListener('mousemove', handleMouseMove);
			window.removeEventListener('mouseup', handleMouseUp);
		}

		node.addEventListener('mousedown', handleMouseDown);

		return {
			destroy() {
				node.removeEventListener('mousedown', handleMouseDown);
				window.removeEventListener('mousemove', handleMouseMove);
				window.removeEventListener('mouseup', handleMouseUp);
			}
		};
	}
</script>

<div
	class="  win95-font flex h-screen w-screen items-center justify-center bg-zinc-900 select-none"
>
	<style>
		.win95-font {
			font-family: 'W95F', sans-serif;
			letter-spacing: 0.75px;
			-webkit-font-smoothing: none;
			font-smooth: never;
			-webkit-font-smoothing: none;
			text-rendering: optimizeSpeed;
			image-rendering: pixelated;
			font-size: 11px;
		}

		/* Standard Win95 Bevel Styles */
		.win95-raised {
			background-color: #c0c0c0;
			border-top: 2px solid #ffffff;
			border-left: 2px solid #ffffff;

			box-shadow:
				inset -1px -1px 0px #808080,
				inset 1px 1px 0px #dfdfdf;
		}

		.win95-window {
			border-right: 1px solid #000000;
			border-bottom: 1px solid #000000;
		}

		.win95-inset {
			border-top: 1px solid #808080;
			border-left: 1px solid #808080;
			border-right: 1px solid #ffffff;
			border-bottom: 1px solid #ffffff;
		}

		.win95-sunken {
			background-color: #ffffff;
			border-top: 2px solid #808080;
			border-left: 2px solid #808080;
			border-right: 2px solid #ffffff;
			border-bottom: 2px solid #ffffff;
			box-shadow:
				inset 1px 1px 0px #000000,
				inset -1px -1px 0px #dfdfdf;
		}

		.win95-titlebar {
			background: linear-gradient(90deg, #000080, #1084d0);
			color: white;
		}

		.win95-btn {
			width: 16px;
			height: 14px;
			background: #c0c0c0;
			border-top: 1px solid #ffffff;
			border-left: 1px solid #ffffff;
			border-right: 1px solid #000000;
			border-bottom: 1px solid #000000;
			box-shadow: inset -1px -1px 0px #808080;
			display: flex;
			align-items: center;
			justify-content: center;
			font-weight: bold;
			font-size: 9px;
			cursor: pointer;
			color: #000;
		}

		.win95-btn:active {
			border-top: 1px solid #000000;
			border-left: 1px solid #000000;
			border-right: 1px solid #ffffff;
			border-bottom: 1px solid #ffffff;
			box-shadow: none;
			padding-top: 1px;
			padding-left: 1px;
		}

		.win95-action-btn {
			background: #c0c0c0;
			border-top: 2px solid #ffffff;
			border-left: 2px solid #ffffff;
			border-right: 2px solid #000000;
			border-bottom: 2px solid #000000;
			box-shadow: inset -1px -1px 0px #808080;
			padding: 2px 8px;
			cursor: pointer;
		}

		.win95-action-btn:active {
			border-top: 2px solid #000000;
			border-left: 2px solid #000000;
			border-right: 2px solid #ffffff;
			border-bottom: 2px solid #ffffff;
			box-shadow: none;
			padding: 3px 7px 1px 9px;
		}
	</style>

	<div class="aspect-[4/3] h-full p-5">
		<div
			class="relative box-border aspect-[4/3] h-full min-h-120 overflow-hidden rounded-2xl border-[32px] border-gray-300 bg-[#008080] shadow-2xl"
		>
			<div class="relative h-[calc(100%-28px)] w-full">
				<div
					use:draggable
					class="win95-raised win95-window absolute w-80 shadow-2xl"
					style="top: 20px; left: 100px;"
				>
					<div
						class="win95-titlebar flex w-79 items-center justify-between px-2 py-0.5 text-xs font-bold"
					>
						<span>What's the deal?</span>
						<div class="no-drag flex gap-1">
							<button class="win95-btn">?</button>
							<button class="win95-btn">✕</button>
						</div>
					</div>

					<div class="flex items-start gap-3 p-3">
						<div>
							<h2 class="mb-1 text-sm font-bold">You ship?</h2>
							<p class="text-xs leading-relaxed">
								Welcome to the Retro World! Bring obsolete devices back to the Internet-connected
								future.
							</p>
						</div>
					</div>

					<div class="flex justify-end gap-2 p-2">
						<button class="win95-action-btn no-drag text-xs">What's New</button>
						<button class="win95-action-btn no-drag text-xs font-bold">OK</button>
					</div>
				</div>
				<!-- 
                <div 
                    use:draggable 
                    class="absolute win95-raised w-72 p-1 shadow-lg"
                    style="top: 140px; left: 240px;"
                >
                    <div class="win95-titlebar px-2 py-0.5 flex items-center justify-between font-bold text-xs">
                        <span>More Info</span>
                        <div class="flex gap-1 no-drag">
                            <button class="win95-btn">_</button>
                            <button class="win95-btn">□</button>
                            <button class="win95-btn">✕</button>
                        </div>
                    </div>

                    <div class="flex gap-3 px-2 py-1 text-xs border-b border-gray-400">
                        <span class="underline">F</span>ile
                        <span class="underline">E</span>dit
                        <span class="underline">V</span>iew
                        <span class="underline">H</span>elp
                    </div>

                    <div class="win95-sunken m-1 p-3 grid grid-cols-2 gap-4 h-36 overflow-y-auto">
                        <div class="flex flex-col items-center cursor-pointer text-center group">
                            <img src={readme} class="w-8 h-8 [image-rendering:pixelated]" alt="Section" />
                            <span class="text-[10px] mt-1 group-hover:bg-[#000080] group-hover:text-white px-0.5">Next Section</span>
                        </div>
                        <div class="flex flex-col items-center cursor-pointer text-center group">
                            <img src={readme} class="w-8 h-8 [image-rendering:pixelated]" alt="Classic App" />
                            <span class="text-[10px] mt-1 group-hover:bg-[#000080] group-hover:text-white px-0.5">Making Classic App</span>
                        </div>
                        <a href="/account/login" class="flex flex-col items-center cursor-pointer text-center group">
                            <img src={finder} class="w-8 h-8 [image-rendering:pixelated]" alt="Account" />
                            <span class="text-[10px] mt-1 group-hover:bg-[#000080] group-hover:text-white px-0.5">Log into Account</span>
                        </a>
                    </div>
                </div>

                <div 
                    use:draggable 
                    class="absolute win95-raised w-64 p-1 shadow-lg"
                    style="top: 180px; left: 30px;"
                >
                    <div class="win95-titlebar px-2 py-0.5 flex items-center justify-between font-bold text-xs">
                        <span>Why.txt - Notepad</span>
                        <div class="flex gap-1 no-drag">
                            <button class="win95-btn">_</button>
                            <button class="win95-btn">□</button>
                            <button class="win95-btn">✕</button>
                        </div>
                    </div>

                    <div class="win95-sunken m-1 p-2 h-28 text-xs font-mono overflow-y-auto leading-tight no-drag">
                        <b>Why?</b><br/><br/>
                        Do you remember back when you could turn on that old laptop in your attic, and just use it normally?
                        <br/><br/>
                        Well, let's fix that!
                    </div>
                </div>
 -->
			</div>

			<div
				class="win95-raised absolute right-0 bottom-0 left-0 z-50 flex h-7 items-center justify-between px-1"
			>
				<button
					class="win95-action-btn flex h-5 items-center gap-1 py-0.5 text-xs font-bold tracking-wider"
				>
					<img src={win95} class="[image-rendering:pixelated]" />
					<span class="font-w95 remove-font-smoothing">Start</span>
				</button>

				<div class="flex flex-1 gap-1 overflow-x-auto px-2">
					<div
						class="win95-sunken flex w-28 items-center gap-1 truncate bg-gray-200 px-2 py-0.5 text-xs font-bold"
					>
						<!--                         <img src={readme} class="w-3.5 h-3.5 [image-rendering:pixelated]" alt="Task Icon" />
 -->
						<span>Welcome</span>
					</div>
				</div>

				<div class="win95-inset flex h-5 items-center gap-2 bg-[#c0c0c0] px-3 py-0.5 text-xs">
					<span>12:47 AM</span>
				</div>
			</div>
		</div>
	</div>
</div>
 -->