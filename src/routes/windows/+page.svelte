<script lang="ts">
    import readme from "$lib/assets/readme.png";
    import finder from "$lib/assets/finder.png";
    import controlstrip from "$lib/assets/controlstrip.png";
    import win95 from "$lib/assets/win95.png";

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

<div class="  w-screen h-screen flex justify-center items-center bg-zinc-900 win95-font select-none">
    <style>
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

    <div class="h-full p-5 aspect-[4/3]">
        <div class="aspect-[4/3] border-[32px] rounded-2xl border-gray-300 box-border relative min-h-120 h-full overflow-hidden shadow-2xl bg-[#008080]">
            
            <div class="relative w-full h-[calc(100%-28px)]">
                <div 
                    use:draggable 
                    class="absolute win95-raised win95-window w-80 shadow-2xl"
                    style="top: 20px; left: 100px;"
                >
                    <div class="win95-titlebar w-79 px-2 py-0.5 flex items-center justify-between font-bold text-xs">
                        <span>What's the deal?</span>
                        <div class="flex gap-1 no-drag">
                            <button class="win95-btn">?</button>
                            <button class="win95-btn">✕</button>
                        </div>
                    </div>

                    <div class="p-3 flex gap-3 items-start">
                        <div>
                            <h2 class="font-bold text-sm mb-1">You ship?</h2>
                            <p class="text-xs leading-relaxed">
                                Welcome to the Retro World! Bring obsolete devices back to the Internet-connected future.
                            </p>
                        </div>
                    </div>

                    <div class="flex justify-end p-2 gap-2">
                        <button class="win95-action-btn text-xs no-drag">What's New</button>
                        <button class="win95-action-btn text-xs font-bold no-drag">OK</button>
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
                        <div class="flex flex-col items-center cursor-pointer text-center group">
                            <img src={finder} class="w-8 h-8 [image-rendering:pixelated]" alt="Account" />
                            <span class="text-[10px] mt-1 group-hover:bg-[#000080] group-hover:text-white px-0.5">Log into Account</span>
                        </div>
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

            <div class="absolute bottom-0 left-0 right-0 h-7 win95-raised flex items-center justify-between px-1 z-50">
                
                <button class="win95-action-btn tracking-wider font-bold flex items-center gap-1 text-xs py-0.5 h-5">
                    <img src={win95} class="[image-rendering:pixelated]">
                    <span class="font-w95 remove-font-smoothing">Start</span>
                </button>

                <div class="flex-1 flex gap-1 px-2 overflow-x-auto">
                    <div class="win95-sunken bg-gray-200 px-2 py-0.5 text-xs flex items-center gap-1 w-28 truncate font-bold">
<!--                         <img src={readme} class="w-3.5 h-3.5 [image-rendering:pixelated]" alt="Task Icon" />
 -->                        <span>Welcome</span>
                    </div>

                </div>

                <div class="win95-inset px-3 py-0.5 text-xs flex items-center gap-2 h-5 bg-[#c0c0c0]">
                    <span>12:47 AM</span>
                </div>

            </div>

        </div>
    </div>
</div>