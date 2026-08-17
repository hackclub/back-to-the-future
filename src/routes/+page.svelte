<script lang="ts">
    import apple from '$lib/assets/item.png';
    import apple2 from '$lib/assets/item2.png';
    import os7folder from '$lib/assets/os7folder.png';
    import controlstrip from '$lib/assets/controlstrip.png';
    import readme from '$lib/assets/readme.png';
    import finder from '$lib/assets/finder.png';
    import win95 from '$lib/assets/win95.png';
    import wincom from '$lib/assets/wincom.png';
    import winfolder from '$lib/assets/winfolder.png';
    import { slide } from 'svelte/transition';
    import { goto } from '$app/navigation';
    import powerbook from '$lib/assets/powerbook.jpg'
    import fdisk from '$lib/assets/fdisk.jpg'
    import ifixit from '$lib/assets/ifixit.jpg'
    import thinkpad from '$lib/assets/thinkpad.jpg'

    let ind = $state(1000);

    function draggable(node: HTMLDivElement) {
        let isDragging = false;
        let startX: number, startY: number;
        let startLeft: number, startTop: number;

        function handleMouseDown(e: MouseEvent) {
            if (e.target.closest('pre')) return;
            if (e.target.closest('[contenteditable]')) return;
            isDragging = true;

            // Get current mouse position
            startX = e.clientX;
            startY = e.clientY;

            // Get current element position (default to 0 if not set)
            startLeft = parseInt(node.style.left) || 0;
            startTop = parseInt(node.style.top) || 0;

            // Listen to window events so dragging continues if mouse moves fast
            window.addEventListener('mousemove', handleMouseMove);
            window.addEventListener('mouseup', handleMouseUp);

            node.style.zIndex = String(ind++);
        }

        function handleMouseMove(e: MouseEvent) {
            if (!isDragging) return;
            window.getSelection()?.removeAllRanges();

            // Calculate how far the mouse has moved
            const dx = e.clientX - startX;
            const dy = e.clientY - startY;

            // Get parent boundaries to restrict movement
            const parent = node.parentElement;
            const parentRect = parent?.getBoundingClientRect();
            const nodeRect = node.getBoundingClientRect();

            // Calculate new proposed positions
            let newLeft = startLeft + dx;
            let newTop = startTop + dy;

            // Keep element within the horizontal boundaries of the parent
            const maxLeft = parentRect!.width - nodeRect.width;
            newLeft = Math.max(0, Math.min(newLeft, maxLeft));

            // Keep element within the vertical boundaries of the parent
            const maxTop = parentRect!.height - nodeRect.height - 24;
            newTop = Math.max(0, Math.min(newTop, maxTop));

            // Update element styles
            node.style.left = `${newLeft}px`;
            node.style.top = `${newTop}px`;
        }

        function handleMouseUp() {
            isDragging = false;
            window.removeEventListener('mousemove', handleMouseMove);
            window.removeEventListener('mouseup', handleMouseUp);
        }

        // Attach initial event listener to the element
        node.addEventListener('mousedown', handleMouseDown);

        // Clean up event listeners when the element is destroyed
        return {
            destroy() {
                node.removeEventListener('mousedown', handleMouseDown);
                window.removeEventListener('mousemove', handleMouseMove);
                window.removeEventListener('mouseup', handleMouseUp);
            }
        };
    }

    let currentScreen = $state(0);
    let currentItemIndex = $state(0);

    let viewportWidth = $state(0);
    let viewportHeight = $state(0);

    // Fixed resolution target for your vintage OS desktop
    const VIRTUAL_WIDTH = 800;
    const VIRTUAL_HEIGHT = 600;

    // Calculate scale factor automatically
    let scale = $derived(
        Math.min(viewportWidth / VIRTUAL_WIDTH, viewportHeight / VIRTUAL_HEIGHT, 1)
    );

    const notes = [
        {
            title: 'JOIN TODAY!!!',
            date: 'Aug 10, 2026',
            content: `This brings us to the end of the demo!
And so, my fellow Hackclubbers: ask not what your old tech can do for you, but what <b>you can do for your old tech.</b>

If you're interested in this, consider the following platforms to begin! Click Join Us! for the submission form and an invitation to the Slack channel!

- Windows 9x/XP/Vista? Use something like the Win32 API to create lightweight binaries on 9x, or Qt, wxWidgets, .NET for Windows XP. (If you're using a more modern framework, try not to rely on the modern facilities you'll be blessed with.)
- Android 1.5-7? Use an older version of Android Studio. Try to aim to use a version of Android Studio released around the time your targeted version of Android was, since that'll make your experience probably as smooth as it can be. Worst case? Use a newer version. (If your selected version of Android Studio doesn't support Wakatime directly, you can use something like wakapi-anyide.)

If you're more advanced, okay with weird troubleshooting, and own a mac, you can try the following:
- OSX 10.0-10.11: You can (try to) use a modern version of Xcode to make an app for older version of OS X. Do your research though, versions before 10.4 will strictly not work past Xcode 3.0 because they all use PPC, and other versions have incompatibilities with i386, requiring Xcode on High Sierra. OSX 10.9 SDK works somewhat okay on Xcode 26.
- iOS 2.0-10: You'll have a lot of luck with iOS 10 if you manage to get the iOS 10 SDK on a modern version of Xcode. Versions below that, like iOS 6 and below, are going to be more difficult. If you want to build for older versions, I do have a version of wakatime that can track your coding time on Xcode built for macOS 10.9, so if you're interested in going for a very old version, then go ahead!
            `
        }
    ];

    let currentNoteIndex = $state(0);
    let isWindowOpen = $state(true);
</script>

<svelte:window bind:innerWidth={viewportWidth} bind:innerHeight={viewportHeight} />

<!-- screen one son -->
<div class="flex h-screen w-screen items-center justify-center transition-all">
    {#if currentScreen == 0}
        <style>
            /*250,218,78 254,251,179*/
            html {
                background: repeating-conic-gradient(#808080 0 25%, #0000 0 50%) 50% / 2px 2px;
            }

            .checkered-yellow-bg {
                background: repeating-conic-gradient(rgb(250, 218, 78) 0 25%, rgb(254, 251, 179) 0 50%) 50% / 2px 2px;
            }

            .checkered-green-bg {
                background: repeating-conic-gradient(rgb(130, 244, 134) 0 25%, rgb(217, 251, 218) 0 50%) 50% / 2px 2px;
            }

            .checkered-blue-bg {
                background: repeating-conic-gradient(rgb(179, 179, 249) 0 25%, rgb(218, 218, 252) 0 50%) 50% / 2px 2px;
            }

            .checkered-purple-bg {
                background: repeating-conic-gradient(rgb(217, 179, 249) 0 25%, rgb(238, 218, 252) 0 50%) 50% / 2px 2px;
            }

            .checkered-pink-bg {
                background: repeating-conic-gradient(rgb(250, 179, 216) 0 25%, rgb(254, 218, 237) 0 50%) 50% / 2px 2px;
            }

            .checkered-gray-bg {
                background: repeating-conic-gradient(rgb(218, 218, 218) 0 25%, rgb(239, 239, 239) 0 50%) 50% / 2px 2px;
            }

            .pinstripe {
                background: repeating-linear-gradient(to bottom, #ffffff 0px, #ffffff 1px, #888888 1px, #888888 2px, #dddddd 2px, #dddddd 3px);
            }

            .win-btn {
                width: 11px;
                height: 11px;
                background: #fff;
                border: 1px solid #000;
                box-shadow: inset -1px -1px 0px #808080;
                padding: 0;
                cursor: pointer;
            }

            br {
                margin-bottom: 4px;
            }
        </style>

        <div
            class="relative origin-center transition-transform duration-75"
            style="width: {VIRTUAL_WIDTH}px; height: {VIRTUAL_HEIGHT}px; transform: scale({scale});"
        >
            <div class="aspect-[4/3] h-full" transition:slide>
                <div class="p-5">
                    <div class="box- relative aspect-[4/3] h-full min-h-120 rounded-2xl border-32 border-gray-200">
                        <div class="h-full rounded-2xl">
                            <div
                                style="font-family: Geneva, sans-serif; font-size: 1px;"
                                class="remove-font-smoothing top-0 z-500 flex h-6 w-full items-center justify-between bg-white font-black"
                            >
                                <img class="" src={apple} />
                                <img class="" src={apple2} />
                            </div>
                            <div class="absolute flex justify-end items-center p-2 w-full remove-font-smoothing" style="font-family: Helvetica, sans-serif">
                                <!-- <button class="z-500 flex flex-col items-center justify-center cursor-pointer" onclick={() => (isWindowOpen = true)}>
                                    <img src={os7folder} class="h-8 w-8 [image-rendering:pixelated]" />
                                    <div class="text-[10px] bg-white">What can I win?</div>
                                </button> -->
                            </div>
                            <div class="absolute h-full w-full">
                                <div
                                    style="top: 16px; left: 16px; font-family: Helvetica, sans-serif"
                                    use:draggable
                                    class="absolute h-max w-96 border-2 border-[#fceb73] bg-[#fdffa9] text-6xl font-bold tracking-wider text-[#fdffa9] font-stretch-condensed [-webkit-text-stroke:2px_black]"
                                >
                                    <div class=" checkered-yellow-bg h-3 w-full"></div>
                                    <span
                                        class="remove-font-smoothing [text-shadow:-2px_-2px_0_#000,_2px_-2px_0_#000,_-2px_2px_0_#000,_2px_2px_0_#000,_5px_5px_0_#000]"
                                        contenteditable="true"
                                    >
                                        Back To The Future
                                    </span>
                                </div>

                                <!-- TODO: this is the ysws shop -->
                                {@debug isWindowOpen}
                                {#if isWindowOpen}
                                    <div
                                        style="top: 40px; left: 380px; font-family: Geneva, sans-serif"
                                        use:draggable
                                        class="absolute h-max w-64 border border-black bg-[rgb(243,243,243)] font-stretch-condensed shadow-2xl z-50"
                                    >
                                        {let windowCollapsed = $state(true)}
                                        <div
                                            class="pinstripe remove-font-smoothing block flex h-4 w-full flex-row items-center justify-between border border-[rgb(218,218,252)] text-xs font-bold"
                                        >
                                            <div class="win-btn mb-0.5 block opacity-0" aria-label="Collapse"></div>
                                            <span class="block h-full bg-[rgb(243,243,243)] px-2 tracking-wider"> Prizes </span>
                                            <div onclick={() =>(windowCollapsed = !windowCollapsed)} class="win-btn mb-0.5 block text-xs" aria-label="Collapse"></div>
                                        </div>
                                        {#if !windowCollapsed}
                                            <div class="h-0.75 border-y-1"></div>
                                            <div class="remove-font-smoothing bg-white p-2 text-xs flex flex-col gap-4 overflow-y-auto max-h-96">
                                                {let currentIndex = $state(0)}
                                                <div class="flex flex-col">
                                                    {#if currentIndex == 0}
                                                        <img src={powerbook}>
                                                        <span class="text-center font-bold text-base">PowerBook G4</span>
                                                        <span class="text-center italic">~40-50 hrs</span>
                                                    {:else if currentIndex == 1}
                                                        <img src={fdisk}>
                                                        <span class="text-center font-bold text-base">Floppy disks</span>
                                                        <span class="text-center italic">~5-6 hrs</span>
                                                    {:else if currentIndex == 2}
                                                        <img src={ifixit}>
                                                        <span class="text-center font-bold text-base">$10 iFixit credit</span>
                                                        <span class="text-center italic">~2-3 hrs</span>
                                                    {:else if currentIndex == 3}    
                                                        <img src={thinkpad}>
                                                        <span class="text-center font-bold text-base">IBM Thinkpad T60</span>
                                                        <span class="text-center italic">~24-30 hrs</span>
                                                    {:else}
                                                        <span class="text-center font-bold text-base">And so much more!</span>
                                                        <span class="text-center">Want a device not listed here? Get a grant to get your own!!! Shop takes requests too!</span>
                                                    {/if}
                                                </div>
                                                <div class="flex flex-row gap-4 justify-center items-center">
                                                    {#if currentIndex != 0}
                                                    <button onclick={() => currentIndex--} class="cursor-pointer select-none rounded-[4px] border-1 border-black bg-white font-bold text-black ring-2 ring-black ring-offset-1 ring-offset-[#f3f3f3] subpixel-antialiased active:bg-black active:text-white w-max px-4">
                                                        Previous
                                                    </button>
                                                    {/if}
                                                    {#if currentIndex != 4}
                                                    <button onclick={() => currentIndex++} class="cursor-pointer select-none rounded-[4px] border-1 border-black bg-white font-bold text-black ring-2 ring-black ring-offset-1 ring-offset-[#f3f3f3] subpixel-antialiased active:bg-black active:text-white w-max px-4">
                                                        Next
                                                    </button>
                                                    {/if}
                                                </div>
                                            </div>
                                        {/if}
                                    </div>
                                {/if}

                                <div
                                    style="top: 240px; left: 408px; font-family: Geneva, sans-serif"
                                    use:draggable
                                    class="absolute h-max w-60 border border-black bg-[rgb(243,243,243)] font-stretch-condensed shadow-2xl"
                                >
                                    {let windowCollapsed = $state(false)}
                                    <div
                                        class="pinstripe remove-font-smoothing block flex h-4 w-full flex-row items-center justify-between border border-[rgb(218,218,252)] text-xs font-bold"
                                    >
                                        <div class="win-btn mb-0.5 block opacity-0" aria-label="Collapse"></div>
                                        <span class="block h-full bg-[rgb(243,243,243)] px-2 tracking-wider"> More Info </span>
                                        <div onclick={(windowCollapsed = !windowCollapsed)} class="win-btn mb-0.5 block text-xs" aria-label="Collapse"></div>
                                    </div>
                                    {#if !windowCollapsed}
                                        <div class="h-0.75 border-y-1"></div>
                                        <div class="remove-font- grid grid-cols-2 bg-white p-2">
                                            <button class="block flex cursor-pointer appearance-none flex-col items-center justify-center" onclick={() => (currentScreen = 1)}>
                                                <img src={readme} class="h-8 w-8 [image-rendering:pixelated]" />
                                                <div class="text-[10px]">Next Section</div>
                                            </button>
                                            <button
                                                class="flex flex-col items-center justify-center cursor-pointer"
                                                onclick={() => window.open('https://forms.hackclub.com/t/gA2V9LjKaDus', '__blank')}
                                            >
                                                <img src={finder} class="h-8 w-8 [image-rendering:pixelated]" />
                                                <div class="text-[10px]">Join us!!!</div>
                                            </button>
                                        </div>
                                    {/if}
                                </div>

                                <div
                                    style="top: 340px; left: 280px; font-family: Geneva, sans-serif"
                                    use:draggable
                                    class="absolute h-max w-84 border border-black bg-[rgb(243,243,243)] font-stretch-condensed shadow-2xl"
                                >
                                    {let windowCollapsed = $state(true)}
                                    <div
                                        class="pinstripe remove-font-smoothing block flex h-4 w-full flex-row items-center justify-between border border-[rgb(218,218,252)] text-xs font-bold"
                                    >
                                        <div class="win-btn mb-0.5 block opacity-0" aria-label="Collapse"></div>
                                        <span class="block h-full bg-[rgb(243,243,243)] px-2 tracking-wider"> Like Classic Macs? (or just apps)</span>
                                        <div onclick={(windowCollapsed = !windowCollapsed)} class="win-btn mb-0.5 block text-xs" aria-label="Collapse"></div>
                                    </div>
                                    {#if !windowCollapsed}
                                        <div class="h-0.75 border-y-1"></div>
                                        <div class="remove-font- grid grid-cols-2 bg-white p-2">
                                            <button class="block flex cursor-pointer appearance-none flex-col items-center justify-center" onclick={() => (currentScreen = 1)}>
                                                <img src={readme} class="h-8 w-8 [image-rendering:pixelated]" />
                                                <div class="text-[10px]">Create an app!</div>
                                            </button>
                                            <div class="flex flex-col items-center justify-center">
                                                <img src={finder} class="h-8 w-8 [image-rendering:pixelated]" />
                                                <div class="text-[10px]">Other guides</div>
                                            </div>
                                        </div>
                                    {/if}
                                </div>

                                <div
                                    use:draggable
                                    class="absolute h-max w-48 border-2 border-[rgb(166,247,175)] bg-[rgb(217,251,218)] text-lg font-extralight tracking-wider font-stretch-condensed"
                                    style="top: 128px; left: 360px;font-family: Geneva, sans-serif"
                                >
                                    <div class=" checkered-green-bg h-3 w-full"></div>
                                    <span class="remove-font-smoothing" contenteditable="true"> a Hack Club YSWS </span>
                                </div>

                                <div
                                    use:draggable
                                    class="absolute h-max w-48 border-2 border-[rgb(255,192,226)] bg-[rgb(254,218,237)] text-xs font-extralight tracking-wider font-stretch-condensed"
                                    style="top: 148px; left: 120px;font-family: Geneva, sans-serif"
                                >
                                    <div class=" checkered-pink-bg h-3 w-full"></div>
                                    <span class="remove-font-smoothing" contenteditable="true"> running until Sept. 7!!! </span>
                                </div>

                                <div
                                    use:draggable
                                    class="absolute h-max w-96 border-2 border-[rgb(198,198,250)] bg-[rgb(218,218,252)] text-sm font-extralight tracking-wider font-stretch-condensed"
                                    style="font-family: Geneva, sans-serif; top: 180px; left:20px;"
                                >
                                    <div class=" checkered-blue-bg h-3 w-full"></div>
                                    <span class="remove-font-smoothing" contenteditable="true">
                                        Bring obsolete devices back to the Internet-connected future. Get cool stuff to make yourself modern.
                                    </span>
                                </div>

                                <div
                                    use:draggable
                                    class="absolute h-max w-72 border-2 border-[rgb(218,218,218)] bg-[rgb(218,218,218)] text-sm font-extralight tracking-wider font-stretch-condensed"
                                    style="font-family: Geneva, sans-serif; top: 422px; left:375px;"
                                >
                                    <div class=" checkered-gray-bg h-3 w-full"></div>
                                    <span class="remove-font-smoothing text-[10px]" contenteditable="true">
                                        made w/l &lt;&gt; by atomtables (adithiya venkatakrishnan)
                                    </span>
                                </div>

                                <div
                                    use:draggable
                                    class="absolute h-max w-60 border-2 border-[rgb(227,198,250)] bg-[rgb(238,218,252)] text-xs font-extralight tracking-wider font-stretch-condensed"
                                    style="font-family: Geneva, sans-serif; top: 268px; left:20px;"
                                >
                                    <div class=" checkered-purple-bg h-3 w-full"></div>
                                    <span class="remove-font-smoothing" contenteditable="true">
                                        <b>Why?</b>
                                        <br />
                                        Do you remember back when you could turn on that old laptop in your attic, and just use it normally? No?
                                        <br />
                                        Well, let's fix that!
                                        <br />
                                        (by the way, click Next Section for more information! This is (mostly) interactive.)
                                    </span>
                                </div>

                                <img src={controlstrip} class="absolute bottom-0 left-0 mb-6" />
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    {:else if currentScreen == 1}
        <style>
            html {
                background-color: #008080;
            }

            .win95-font {
                font-family: 'W95F', sans-serif;
                letter-spacing: 0.75px;
/*                -webkit-font-smoothing: none;
                font-smooth: never;
                -webkit-font-smoothing: none;
                text-rendering: optimizeSpeed;
                image-rendering: pixelated;*/
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

            .win95-btn:active:enabled {
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

        <div
            class="relative origin-center transition-transform duration-75"
            style="width: {VIRTUAL_WIDTH}px; height: {VIRTUAL_HEIGHT}px; transform: scale({scale});"
        >
            <div class="win95-font aspect-[4/3] h-full" transition:slide>
                <div class="h-full p-5">
                    <div class="relative box-border aspect-[4/3] h-full min-h-120 overflow-hidden rounded-2xl border-[32px] border-gray-300 bg-[#008080] shadow-2xl">
                        <div class="relative h-[calc(100%-28px)] w-full">
                            <div use:draggable class="win95-raised win95-window absolute w-80 shadow-2xl" style="top: 20px; left: 32px;">
                                {@debug currentItemIndex}
                                <div class="win95-titlebar flex w-79 items-center justify-between px-2 py-0.5 text-xs font-bold">
                                    <span>What's the deal? (INTERACTIVE!!!)</span>
                                    <div class="no-drag flex gap-1">
                                        <button class="win95-btn">?</button>
                                        <button class="win95-btn">✕</button>
                                    </div>
                                </div>

                                {#if currentItemIndex == 0}
                                    <div class="flex items-start gap-3 p-3">
                                        <div>
                                            <h2 class="mb-1 text-sm font-bold">You ship?</h2>
                                            <p class="text-xs font-bold leading-relaxed">
                                                Something new, something old.<br />
                                                or something never seen before.
                                            </p>
                                        </div>
                                    </div>
                                {:else if currentItemIndex == 1}
                                    <div class="flex items-start gap-3 p-3">
                                        <div>
                                            <h2 class="mb-1 text-sm font-bold">We ship?</h2>
                                            <p class="text-xs font-bold leading-relaxed">
                                                Something tried, something true,<br />
                                                or something worthy of the blue.
                                            </p>
                                        </div>
                                    </div>
                                {:else if currentItemIndex == 2}
                                    <div class="flex items-start gap-3 p-3">
                                        <div>
                                            <h2 class="mb-1 text-sm font-bold">The gist</h2>
                                            <ul class="list-inside font-bold list-disc">
                                                <li>Create a new app that <i>backports</i> functionality from modern day.</li>
                                                <li>
                                                    Patch an older app to <i>restore</i> functionality to work with modern day.
                                                </li>
                                                <li>
                                                    Make a regular app, something you like, and have it be <i>backwards-compatible</i>
                                                    with your chosen platform.
                                                </li>
                                            </ul>
                                        </div>
                                    </div>
                                {:else if currentItemIndex == 3}
                                    <div class="flex items-start gap-3 p-3">
                                        <div>
                                            <h2 class="mb-1 text-sm font-bold">And you get?</h2>
                                            <ul class="list-inside font-bold list-disc">
                                                <li>A grant to get old technology, maybe to even start your next project.</li>
                                                <li>A new gadget, part, or item (like a USB hard drive or 256MB ddr2 RAM) as an upgrade.</li>
                                                <li>An online gift card to sites like iFixit that sell parts and tools for you to keep good tech from being e-waste.</li>
                                            </ul>
                                        </div>
                                    </div>
                                {/if}

                                <div class="flex justify-end gap-2 p-2">
                                    <button class="win95-action-btn no-drag text-xs" onclick={() => currentItemIndex != 0 && currentItemIndex--}>Previous </button>
                                    {#if currentItemIndex != 3}
                                        <button class="win95-action-btn no-drag text-xs font-bold" onclick={() => currentItemIndex++}>
                                            {currentItemIndex == 1 ? 'Yo unc speak in english' : 'Next'}
                                        </button>
                                    {/if}
                                </div>
                            </div>

                            <div use:draggable class="win95-raised win95-window absolute w-72 shadow-2xl" style="top: 72px; left: 348px;">
                                <div class="win95-titlebar flex items-center justify-between px-2 py-0.5 text-xs font-bold">
                                    <span>More Info</span>
                                    <div class="no-drag flex gap-1">
                                        <button class="win95-btn">_</button>
                                        <button class="win95-btn">□</button>
                                        <button class="win95-btn">✕</button>
                                    </div>
                                </div>

                                <div class="flex gap-3 border-b border-gray-400 px-2 py-1 text-xs">
                                    <span><span class="underline">F</span>ile</span>
                                    <span><span class="underline">E</span>dit</span>
                                    <span><span class="underline">V</span>iew</span>
                                    <span><span class="underline">H</span>elp</span>
                                </div>

                                <div class="win95-sunken m-1 grid h-36 grid-cols-2 gap-4 overflow-y-auto p-3">
                                    <button onclick={() => currentScreen--} class="group flex cursor-pointer flex-col items-center text-center">
                                        <img src={winfolder} class="h-8 w-8 [image-rendering:pixelated]" alt="Section" />
                                        <span class="mt-1 px-0.5 text-xs font-bold group-hover:bg-[#000080] group-hover:text-white">Previous Section</span>
                                    </button>
                                    <button onclick={() => currentScreen++} class="group flex cursor-pointer flex-col items-center text-center">
                                        <img src={winfolder} class="h-8 w-8 [image-rendering:pixelated]" alt="Section" />
                                        <span class="mt-1 px-0.5 text-xs font-bold group-hover:bg-[#000080] group-hover:text-white">Next Section</span>
                                    </button>
                                    <div class="group flex cursor-pointer flex-col items-center text-center">
                                        <img src={win95} class="h-8 w-8 [image-rendering:pixelated]" alt="Classic App" />
                                        <span class="mt-1 px-0.5 text-xs font-bold group-hover:bg-[#000080] group-hover:text-white">Make a Windows app!</span>
                                    </div>
                                    <button
                                        onclick={() => window.open('https://forms.hackclub.com/t/gA2V9LjKaDus', '__blank')}
                                        class="group flex cursor-pointer flex-col items-center text-center"
                                    >
                                        <img src={wincom} class="h-8 w-8 [image-rendering:pixelated]" alt="Account" />
                                        <span class="mt-1 px-0.5 text-xs font-bold group-hover:bg-[#000080] group-hover:text-white">Join us!!!</span>
                                    </button>
                                </div>
                            </div>

                            <div use:draggable class="win95-raised absolute w-108 shadow-2xl" style="top: 268px; left: 16px;">
                                <div class="win95-titlebar flex items-center justify-between px-2 py-0.5 text-xs font-bold">
                                    <span>Why.txt - Notepad</span>
                                    <div class="no-drag flex gap-1">
                                        <button class="win95-btn">_</button>
                                        <button class="win95-btn">□</button>
                                        <button class="win95-btn">✕</button>
                                    </div>
                                </div>

                                <div class="win95-sunken no-drag m-1 h-28 overflow-y-auto p-2 font-mono text-xs leading-tight">
                                    <pre
                                        contenteditable="true"
                                        class="whitespace-pre-wrap">If you're between the ages of 13-18, there might be a time in your infancy where you saw a computer from the '00s actually connect to the Internet.<br
                                        /><br
                                        />If you miss that, then this You-Ship-We-Ship is for YOU!!! Yes you, that one person who's been looking for a reason to mess around with that ancient laptop in the attic! And you over there who wants to try to do something with a phone from before you were born! and ESPECIALLY you, that person who wants to save a piece of history from the landfill, or worse, ebay...
                                    </pre>
                                </div>
                            </div>
                        </div>

                        <div class="absolute bottom-6.5 right-0 text-white text-right p-0.5">
                            <div>Back to the Future</div>
                            <div>Still by atomtables (adithiya venkatakrishnan)</div>
                        </div>

                        <div class="win95-raised absolute right-0 bottom-0 left-0 z-50 flex h-7 items-center justify-between px-1">
                            <button class="win95-action-btn flex h-5 items-center gap-1 py-0.5 text-xs font-bold tracking-wider">
                                <img src={win95} class="[image-rendering:pixelated]" />
                                <span class="font-w95 remove-font-smoothing">Start</span>
                            </button>

                            <div class="flex flex-1 gap-1 overflow-x-auto px-2">
                                <div class="win95-sunken flex w-28 items-center gap-1 truncate bg-gray-200 px-2 py-0.5 text-xs font-bold">
                                    <img src={readme} class="h-3.5 w-3.5 [image-rendering:pixelated]" alt="Task Icon" />
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
        </div>
    {:else if currentScreen == 2}
        <style>
            /* Classic iOS Linen Background */
            body {
                background-image: url('/beloved_texture.jpg');
                background-size: 25% 25%;
                background-repeat: repeat;
            }

            /* Skeuomorphic Leather Header */
            .ios-leather {
                background: linear-gradient(to bottom, #6b4d36, #412a1a);
                border-bottom: 2px solid #20130a;
                box-shadow:
                    inset 0 1px 1px rgba(255, 255, 255, 0.3),
                    0 4px 6px rgba(0, 0, 0, 0.4);
                position: relative;
            }

            /* Stitched detailing along the leather */
            .ios-leather::after {
                position: absolute;
                bottom: 2px;
                left: 2px;
                right: 2px;
                height: 100%;
                border-bottom: 1px dashed rgba(0, 0, 0, 0.5);
                box-shadow: 0 1px 0 rgba(255, 255, 255, 0.1);
                pointer-events: none;
            }

            .ios-font {
                font-family: 'Marker Felt', 'Comic Sans MS', 'Chalkboard SE', cursive, sans-serif;
            }

            .ios-sans {
                font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
            }

            .ios-paper {
                background-color: #fdf6e3;
                background-image: 
            /* Red Margin Line */
                    linear-gradient(90deg, transparent 40px, rgba(234, 153, 153, 0.8) 40px, rgba(234, 153, 153, 0.8) 42px, transparent 42px),
                    /* Blue Ruled Lines */ repeating-linear-gradient(to bottom, transparent, transparent 31px, rgba(160, 190, 220, 0.6) 31px, rgba(160, 190, 220, 0.6) 32px);
                background-size:
                    100% 100%,
                    100% 32px;
                background-attachment: local;
                box-shadow: inset 5px 0 15px rgba(0, 0, 0, 0.05);
            }

            .ios-sidebar-paper {
                background-color: #f5eedc;
                background-image: repeating-linear-gradient(to bottom, transparent, transparent 43px, rgba(0, 0, 0, 0.05) 43px, rgba(0, 0, 0, 0.05) 44px);
                border-right: 1px solid #d4cca6;
            }

            /* Glossy 3D buttons */
            .ios-btn {
                background: linear-gradient(to bottom, #a07a60, #63432e);
                border: 1px solid #332013;
                box-shadow:
                    inset 0 1px 0 rgba(255, 255, 255, 0.2),
                    0 1px 2px rgba(0, 0, 0, 0.4);
                border-radius: 6px;
                color: #fff;
                text-shadow: 0 -1px 0 rgba(0, 0, 0, 0.7);
                padding: 4px 12px;
                font-size: 12px;
                font-weight: bold;
                cursor: pointer;
            }

            .ios-btn:active {
                background: linear-gradient(to bottom, #63432e, #a07a60);
                box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.5);
            }
        </style>
        <div
            class="relative origin-center transition-transform duration-75"
            style="width: {VIRTUAL_WIDTH}px; height: {VIRTUAL_HEIGHT}px; transform: scale({scale});"
        >
        <div class="aspect-[4/3] h-full" transition:slide>
            <div class="h-full p-5">
                <div class="relative box-border aspect-[4/3] h-full min-h-120 overflow-hidden rounded-3xl border-[24px] border-black bg-black shadow-2xl">
                    <div class="ios-linen-bg relative h-full w-full overflow-hidden rounded-md">
                        <div class="ios-sans z-50 flex h-5 w-full items-center justify-between bg-black px-2 text-[10px] font-bold text-gray-300">
                            <div class="flex items-center gap-1">
                                <span>iPad</span>
                            </div>
                            <span>12:47 AM</span>
                            <div class="flex items-center gap-1">
                                <span>100%</span>
                                <div class="h-2.5 w-5 rounded-sm border border-gray-400 p-[1px]">
                                    <div class="h-full w-full bg-white"></div>
                                </div>
                            </div>
                        </div>

                        <div class="absolute flex overflow-hidden rounded-lg shadow-2xl w-full h-full" style="">
                            <div class="ios-sidebar-paper flex h-full w-48 flex-col">
                                <div class="ios-leather after:left-2 after:bottom-2 after:right-2 flex h-12 shrink-0 items-center justify-between px-3">
                                    <button onclick={() => window.open('https://forms.hackclub.com/t/gA2V9LjKaDus', '__blank')} class="ios-btn ios-sans">Join Us!</button>
                                    <span class="ios-sans text-sm font-bold text-white text-shadow-sm [text-shadow:0_-1px_0_rgba(0,0,0,0.7)]">Notes</span>
                                    <button class="ios-btn ios-sans">+</button>
                                </div>

                                <div class="flex-1 overflow-y-auto">
                                    {#each notes as note, i}
                                        <div
                                            onclick={() => (currentNoteIndex = i)}
                                            class="ios-font flex cursor-pointer flex-col justify-center border-b border-gray-300/50 px-4 py-2 hover:bg-yellow-900/5 {currentNoteIndex ===
                                            i
                                                ? 'bg-yellow-900/10'
                                                : ''}"
                                        >
                                            <div class="truncate text-base font-bold text-gray-800">{note.title}</div>
                                            <div class="text-xs text-gray-500">{new Date().toLocaleDateString()}</div>
                                        </div>
                                    {/each}
                                    <div
                                        onclick={() => window.open('https://hackclub.enterprise.slack.com/docs/T0266FRGM/F0BPZ1RLY0L', '__blank')}
                                        class="ios-font flex cursor-pointer flex-col justify-center border-b border-gray-300/50 px-4 py-2 hover:bg-yellow-900/5"
                                    >
                                        <div class="truncate text-base font-bold text-gray-800">FAQ</div>
                                        <div class="text-xs text-gray-500">{new Date().toLocaleDateString()}</div>
                                    </div>
                                </div>
                            </div>

                            <div class="flex h-full flex-1 flex-col bg-[#fdf6e3]">
                                <div class="ios-leather flex h-12 shrink-0 items-center justify-between px-3">
                                    <div></div>
                                    <div class="flex gap-2">
                                        <button onclick={currentScreen--} class="ios-btn ios-sans text-lg leading-none">Previous Section</button>
                                    </div>
                                </div>

                                <div class="ios-paper h-full flex-1 overflow-y-auto">
                                    {#key currentNoteIndex}
                                        <div class="p-8 pl-14">
                                            <div class="ios-font text-gray-800">
                                                <div class="mb-4 text-center text-sm text-gray-400">{new Date().toLocaleDateString()}</div>
                                                <h1 class="mb-4 text-2xl font-bold">{notes[currentNoteIndex].title}</h1>

                                                <pre contenteditable="true" class="ios-font whitespace-pre-wrap text-lg leading-[32px] text-gray-700 outline-none">{@html notes[
                                                        currentNoteIndex
                                                    ].content}</pre>
                                            </div>
                                        </div>
                                    {/key}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    {/if}
</div>

<div class="max-sm:block hidden fixed top-8 text-black font-sans font-bold bg-white w-full text-center text-sm">
    You should use Landscape mode for the best experience!
</div>