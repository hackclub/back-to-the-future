<script lang="ts">
    import apple from "$lib/assets/item.png";
    import apple2 from "$lib/assets/item2.png";
	import controlstrip from "$lib/assets/controlstrip.png";
    import readme from "$lib/assets/readme.png";
    import finder from "$lib/assets/finder.png";
    import win95 from "$lib/assets/win95.png";
    import wincom from "$lib/assets/wincom.png";
    import winfolder from "$lib/assets/winfolder.png";
    import {slide} from "svelte/transition"

    let ind = $state(1000);

    function draggable(node) {
        let isDragging = false;
        let startX, startY;
        let startLeft, startTop;

        function handleMouseDown(e) {
            if (e.target.closest("pre")) return;
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

          node.style.zIndex = ind++;
        }

        function handleMouseMove(e) {
          if (!isDragging) return;
          window.getSelection().removeAllRanges();
          
          // Calculate how far the mouse has moved
          const dx = e.clientX - startX;
          const dy = e.clientY - startY;
          
          // Get parent boundaries to restrict movement
          const parent = node.parentElement;
          const parentRect = parent.getBoundingClientRect();
          const nodeRect = node.getBoundingClientRect();
          
          // Calculate new proposed positions
          let newLeft = startLeft + dx;
          let newTop = startTop + dy;
          
          // Keep element within the horizontal boundaries of the parent
          const maxLeft = parentRect.width - nodeRect.width;
          newLeft = Math.max(0, Math.min(newLeft, maxLeft));
          
          // Keep element within the vertical boundaries of the parent
          const maxTop = parentRect.height - nodeRect.height;
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

  let currentScreen = $state(1);
</script>

<!-- screen one son -->
<div class="w-screen h-screen flex justify-center items-center transition-all">
  
    {#if currentScreen == 0}
    <style>
        /*250,218,78 254,251,179*/
        html {
            background: repeating-conic-gradient(#808080 0 25%, #0000 0 50%) 50% / 2px 2px;
        }

        .checkered-yellow-bg {
            background: repeating-conic-gradient(rgb(250,218,78) 0 25%, rgb(254,251,179) 0 50%) 50% / 2px 2px;
        }

        .checkered-green-bg {
            background: repeating-conic-gradient(rgb(130,244,134) 0 25%, rgb(217,251,218) 0 50%) 50% / 2px 2px;
        }

        .checkered-blue-bg {
            background: repeating-conic-gradient(rgb(179,179,249) 0 25%, rgb(218,218,252) 0 50%) 50% / 2px 2px;
        }

        .checkered-purple-bg {
            background: repeating-conic-gradient(rgb(217,179,249) 0 25%, rgb(238,218,252) 0 50%) 50% / 2px 2px;
        }

        .checkered-pink-bg {
            background: repeating-conic-gradient(rgb(250,179,216) 0 25%, rgb(254,218,237) 0 50%) 50% / 2px 2px;
        }

        .checkered-gray-bg {
            background: repeating-conic-gradient(rgb(218,218,218) 0 25%, rgb(239,239,239) 0 50%) 50% / 2px 2px;
        }

        .pinstripe {
            background: repeating-linear-gradient(
                to bottom,
                #ffffff 0px,
                #ffffff 1px,
                #888888 1px,
                #888888 2px,
                #dddddd 2px,
                #dddddd 3px
            );
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

    <div class="h-full aspect-[4/3]" transition:slide>
        <div class="p-5">
        <div class="aspect-[4/3] border-32 rounded-2xl border-gray-200 box- relative min-h-120 h-full">
            <div class="rounded-2xl h-full">
                <div style="font-family: Geneva, sans-serif; font-size: 1px;" class="font-black remove-font-smoothing  top-0 h-6  bg-white z-500 flex items-center justify-between  w-full">
                    <img class="" src={apple} />
                    <img class="" src={apple2} />
                </div>
                <div class="absolute h-full w-full">
                    <div style="top: 16px; left: 16px; font-family: Helvetica, sans-serif" use:draggable class="absolute bg-[#fdffa9] w-96 h-max text-6xl font-bold tracking-wider text-[#fdffa9] [-webkit-text-stroke:2px_black] border-[#fceb73] border-2 font-stretch-condensed" >
                      <div class=" w-full h-3 checkered-yellow-bg">
                            
                      </div>
                      <span class="remove-font-smoothing [text-shadow:-2px_-2px_0_#000,_2px_-2px_0_#000,_-2px_2px_0_#000,_2px_2px_0_#000,_5px_5px_0_#000]">
                          Back To The Future
                      </span></div>

                <div style="top: 240px; left: 280px; font-family: Geneva, sans-serif" use:draggable class="absolute bg-[rgb(243,243,243)] w-60 h-max border-black border shadow-2xl font-stretch-condensed" >
                        <div class="text-xs font-bold block border border-[rgb(218,218,252)] w-full h-4 pinstripe remove-font-smoothing flex flex-row items-center justify-between">
                            <div class="win-btn block mb-0.5" aria-label="Collapse"></div>  
                            <span class="bg-[rgb(243,243,243)] h-full tracking-wider px-2 block">More Info</span>
                            <div class="win-btn block mb-0.5" aria-label="Collapse"></div>  
                        </div>
                        <div class="border-y-1 h-0.75"></div>
                        <div class="remove-font- grid grid-cols-2 bg-white p-2">
                            <button class="appearance-none block cursor-pointer flex flex-col justify-center items-center" onclick={() => currentScreen = 1}>
                                <img src={readme} class="w-8 h-8 [image-rendering:pixelated]">
                                <div class="text-[10px]">Next Section</div>
                            </button>
                            <div class="flex flex-col justify-center items-center">
                                <img src={readme} class="w-8 h-8 [image-rendering:pixelated]">
                                <div class="text-[10px]">Making a Classic app</div>
                            </div>

                            <div class="flex flex-col justify-center items-center">
                                <img src={finder} class="w-8 h-8 [image-rendering:pixelated]">
                                <div class="text-[10px]">Log into your account</div>
                            </div>
                        </div></div>

                <div use:draggable class="absolute bg-[rgb(217,251,218)] w-48 h-max text-lg font-extralight tracking-wider border-[rgb(166,247,175)] border-2 font-stretch-condensed" style="top: 128px; left: 360px;font-family: Geneva, sans-serif">
                    <div class=" w-full h-3 checkered-green-bg">
                        
                    </div>
                    <span class="remove-font-smoothing">
                        a Hack Club YSWS
                    </span></div>

                <div use:draggable class="absolute bg-[rgb(218,218,252)] w-96 h-max text-sm font-extralight tracking-wider border-[rgb(198,198,250)] border-2 font-stretch-condensed" style="font-family: Geneva, sans-serif; top: 180px; left:20px;">
                    <div class=" w-full h-3 checkered-blue-bg">
                        
                    </div>
                    <span class="remove-font-smoothing">
                        Bring obsolete devices back to the Internet-connected future. Get cool stuff to make yourself modern.
                    </span></div>

                <div use:draggable class="absolute bg-[rgb(238,218,252)] w-60 h-max text-xs font-extralight tracking-wider border-[rgb(227,198,250)] border-2 font-stretch-condensed" style="font-family: Geneva, sans-serif; top: 240px; left:20px;">
                    <div class=" w-full h-3 checkered-purple-bg">
                        
                    </div>
                    <span class="remove-font-smoothing">
                        <b>Why?</b>
                        <br>
                        Do you remember back when you could turn on that old
                        laptop in your attic, and just use it normally? No?
                        <br>
                        Well, let's fix that! 
                    </span></div>
          
        <img src={controlstrip} class="absolute bottom-0 left-0 mb-6">  
        
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
            -webkit-font-smoothing: none;
            font-smooth: never;
            -webkit-font-smoothing : none;
            text-rendering: optimizeSpeed;
            image-rendering: pixelated;
            font-size: 11px;
        }

        /* Standard Win95 Bevel Styles */
        .win95-raised {
            background-color: #c0c0c0;
            border-top: 2px solid #ffffff;
            border-left: 2px solid #ffffff;
            
            box-shadow: inset -1px -1px 0px #808080, inset 1px 1px 0px #dfdfdf;
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
            box-shadow: inset 1px 1px 0px #000000, inset -1px -1px 0px #dfdfdf;
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

    <div class="h-full aspect-[4/3] win95-font" transition:slide>
        <div class="p-5 h-full">
        <div class="aspect-[4/3] border-[32px] rounded-2xl border-gray-300 box-border relative min-h-120 h-full overflow-hidden shadow-2xl bg-[#008080]">
            
            <div class="relative w-full h-[calc(100%-28px)]">
                <div 
                    use:draggable 
                    class="absolute win95-raised win95-window w-80 shadow-2xl"
                    style="top: 20px; left: 32px;"
                >
                    {let currentItemIndex = $state(0)}
                    {@debug currentItemIndex}
                    <div class="win95-titlebar w-79 px-2 py-0.5 flex items-center justify-between font-bold text-xs">
                        <span>What's the deal? (INTERACTIVE!!!)</span>
                        <div class="flex gap-1 no-drag">
                            <button class="win95-btn">?</button>
                            <button class="win95-btn">✕</button>
                        </div>
                    </div>

                    {#if currentItemIndex == 0}
                    <div class="p-3 flex gap-3 items-start">
                        <div>
                            <h2 class="font-bold text-sm mb-1">You ship?</h2>
                            <p class="text-xs leading-relaxed">
                                Something new, something old.<br>
                                or something never seen before.
                            </p>
                        </div>
                    </div>
                    {:else if currentItemIndex == 1}
                    <div class="p-3 flex gap-3 items-start">
                        <div>
                            <h2 class="font-bold text-sm mb-1">We ship?</h2>
                            <p class="text-xs leading-relaxed">
                                Something tried, something true,<br>
                                or something worthy of the blue.
                            </p>
                        </div>
                    </div>
                    {:else if currentItemIndex == 2}
                    <div class="p-3 flex gap-3 items-start">
                        <div>
                            <h2 class="font-bold text-sm mb-1">The gist</h2>
                            <ul class="list-disc list-inside">
                                <li>Create a new app that <i>backports</i> functionality from modern day.</li>
                                <li>Patch an older app to <i>restore</i> functionality to work with modern day.</li>
                                <li>Make a regular app, something you like, and have it be <i>backwards-compatible</i> with your chosen platform.</li>
                            </ul>
                        </div>
                    </div>
                    {:else if currentItemIndex == 3}
                    <div class="p-3 flex gap-3 items-start">
                        <div>
                            <h2 class="font-bold text-sm mb-1">And you get?</h2>
                            <ul class="list-disc list-inside">
                                <li>A grant to get old technology, maybe to even start your next project.</li>
                                <li>A new gadget, part, or item (like a USB hard drive or 256MB ddr2 RAM) as an upgrade.</li>
                                <li>An online gift card to sites like iFixit that sell parts and tools for you to keep good tech from being e-waste.</li>
                            </ul>
                        </div>
                    </div>
                    {/if}

                    <div class="flex justify-end p-2 gap-2">
                        <button class="win95-action-btn text-xs no-drag" onclick={()=> (currentItemIndex != 0 && currentItemIndex--)}>Previous</button>
                       {#if currentItemIndex != 3}
                        <button class="win95-action-btn text-xs font-bold no-drag" onclick={() => currentItemIndex++}>
                          {currentItemIndex == 1 ? "Yo unc speak in english" : "Next"}
                        </button>
                        {/if}
                    </div>
                </div>

                <div 
                    use:draggable 
                    class="absolute win95-raised w-72 p-1 shadow-lg"
                    style="top: 72px; left: 348px;"
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
                        <span><span class="underline">F</span>ile</span>
                        <span><span class="underline">E</span>dit</span>
                        <span><span class="underline">V</span>iew</span>
                        <span><span class="underline">H</span>elp</span>
                    </div>

                    <div class="win95-sunken m-1 p-3 grid grid-cols-2 gap-4 h-36 overflow-y-auto">
                        <button onclick={() => currentScreen--} class="flex flex-col items-center cursor-pointer text-center group">
                            <img src={winfolder} class="w-8 h-8 [image-rendering:pixelated]" alt="Section" />
                            <span class="text-[10px] mt-1 group-hover:bg-[#000080] group-hover:text-white px-0.5">Previous Section</span>
                        </button>
                        <button onclick={() => currentScreen++} class="flex flex-col items-center cursor-pointer text-center group">
                            <img src={winfolder} class="w-8 h-8 [image-rendering:pixelated]" alt="Section" />
                            <span class="text-[10px] mt-1 group-hover:bg-[#000080] group-hover:text-white px-0.5">Next Section</span>
                        </button>
                        <div class="flex flex-col items-center cursor-pointer text-center group">
                            <img src={win95} class="w-8 h-8 [image-rendering:pixelated]" alt="Classic App" />
                            <span class="text-[10px] mt-1 group-hover:bg-[#000080] group-hover:text-white px-0.5">Making a Windows App</span>
                        </div>
                        <div class="flex flex-col items-center cursor-pointer text-center group">
                            <img src={wincom} class="w-8 h-8 [image-rendering:pixelated]" alt="Account" />
                            <span class="text-[10px] mt-1 group-hover:bg-[#000080] group-hover:text-white px-0.5">Log into Account</span>
                        </div>
                    </div>
                </div>

                <div 
                    use:draggable 
                    class="absolute win95-raised w-108 p-1 shadow-lg"
                    style="top: 268px; left: 16px;"
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
                        <pre contenteditable="true" class="whitespace-pre-wrap">
If you're between the ages of 13-18, there might be a time in your infancy where you saw a computer from the '00s actually connect to the Internet.

If you miss that, then this You-Ship-We-Ship is for YOU!!! Yes you, that one person who's been looking for a reason to mess around with that ancient laptop in the attic! And you over there who wants to try to do something with a phone from before you were born! and ESPECIALLY you, that person who wants to save a piece of history from the landfill, or worse, ebay...
                        </pre>
                    </div>
                </div>

            </div>

            <div class="absolute bottom-0 left-0 right-0 h-7 win95-raised flex items-center justify-between px-1 z-50">
                
                <button class="win95-action-btn tracking-wider font-bold flex items-center gap-1 text-xs py-0.5 h-5">
                    <img src={win95} class="[image-rendering:pixelated]">
                    <span class="font-w95 remove-font-smoothing">Start</span>
                </button>

                <div class="flex-1 flex gap-1 px-2 overflow-x-auto">
                    <div class="win95-sunken bg-gray-200 px-2 py-0.5 text-xs flex items-center gap-1 w-28 truncate font-bold">
                        <img src={readme} class="w-3.5 h-3.5 [image-rendering:pixelated]" alt="Task Icon" />
                        <span>Welcome</span>
                    </div>

                </div>

                <div class="win95-inset px-3 py-0.5 text-xs flex items-center gap-2 h-5 bg-[#c0c0c0]">
                    <span>12:47 AM</span>
                </div>

            </div>

        </div>
    </div>
    </div>
    {/if}
    

</div>