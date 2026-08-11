<script lang="ts">
    import { slide, fade } from 'svelte/transition';
    import { goto } from '$app/navigation';
    import beloved_texture from "$lib/assets/beloved_texture.jpg";

    let ind = $state(1000);

    const notes = [
        {
            title: 'Back To The Future',
            date: 'Aug 10, 2026',
            content: 'Bring obsolete devices back to the Internet-connected future. Get cool stuff to make yourself modern.\n\n(by the way, you can interact with this iPad!)'
        },
        {
            title: 'Why?',
            date: 'Aug 9, 2026',
            content: "Do you remember back when you could turn on that old laptop in your attic, and just use it normally? No?\n\nWell, let's fix that! If you're between the ages of 13-18, there might be a time in your infancy where you saw a computer from the '00s actually connect to the Internet.\n\nIf you miss that, then this You-Ship-We-Ship is for YOU!!!"
        },
        {
            title: 'The Gist',
            date: 'Aug 8, 2026',
            content: '• Create a new app that backports functionality from modern day.\n\n• Patch an older app to restore functionality to work with modern day.\n\n• Make a regular app, something you like, and have it be backwards-compatible with your chosen platform.'
        },
        {
            title: 'And you get?',
            date: 'Aug 7, 2026',
            content: '• A grant to get old technology, maybe to even start your next project.\n\n• A new gadget, part, or item (like a USB hard drive or 256MB ddr2 RAM) as an upgrade.\n\n• An online gift card to sites like iFixit that sell parts and tools for you to keep good tech from being e-waste.'
        }
    ];

    let currentNoteIndex = $state(0);
</script>

<style>
    /* Classic iOS Linen Background */

    /* Skeuomorphic Leather Header */
    .ios-leather {
        background: linear-gradient(to bottom, #6b4d36, #412a1a);
        border-bottom: 2px solid #20130a;
        box-shadow: inset 0 1px 1px rgba(255, 255, 255, 0.3), 0 4px 6px rgba(0, 0, 0, 0.4);
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

    /* Marker Felt replacement stack */
    .ios-font {
        font-family: 'Marker Felt', 'Comic Sans MS', 'Chalkboard SE', cursive, sans-serif;
    }

    .ios-sans {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    /* Yellow ruled paper with the classic red margin */
    .ios-paper {
        background-color: #fdf6e3;
        background-image: 
            /* Red Margin Line */
            linear-gradient(90deg, transparent 40px, rgba(234, 153, 153, 0.8) 40px, rgba(234, 153, 153, 0.8) 42px, transparent 42px),
            /* Blue Ruled Lines */
            repeating-linear-gradient(to bottom, transparent, transparent 31px, rgba(160, 190, 220, 0.6) 31px, rgba(160, 190, 220, 0.6) 32px);
        background-size: 100% 100%, 100% 32px;
        background-attachment: local;
        box-shadow: inset 5px 0 15px rgba(0,0,0,0.05);
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
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.2), 0 1px 2px rgba(0,0,0,0.4);
        border-radius: 6px;
        color: #fff;
        text-shadow: 0 -1px 0 rgba(0,0,0,0.7);
        padding: 4px 12px;
        font-size: 12px;
        font-weight: bold;
        cursor: pointer;
    }

    .ios-btn:active {
        background: linear-gradient(to bottom, #63432e, #a07a60);
        box-shadow: inset 0 1px 3px rgba(0,0,0,0.5);
    }
</style>

<div class="ios-linen-bg flex h-screen w-screen items-center justify-center transition-all bg-repeat" style:background-image="url('{beloved_texture}')" style:background-size="25% 25%">
    <div class="aspect-[4/3] h-full" transition:slide>
        <div class="h-full p-5">
            <div class="relative box-border aspect-[4/3] h-full min-h-120 overflow-hidden rounded-3xl border-[24px] border-black bg-black shadow-2xl">
                <div class="ios-linen-bg relative h-full w-full overflow-hidden rounded-md">
                    
                    <div class="ios-sans z-50 flex h-5 w-full items-center justify-between bg-black px-2 text-[10px] font-bold text-gray-300">
                        <div class="flex items-center gap-1">
                            <span>iPad</span>
                            <svg class="h-3 w-3 fill-current" viewBox="0 0 24 24"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"/></svg>
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
                                <button onclick={() => goto('/')} class="ios-btn ios-sans">Accounts</button>
                                <span class="ios-sans text-sm font-bold text-white text-shadow-sm [text-shadow:0_-1px_0_rgba(0,0,0,0.7)]">Notes</span>
                                <button class="ios-btn ios-sans">+</button>
                            </div>

                            <div class="flex-1 overflow-y-auto">
                                {#each notes as note, i}
                                    <div 
                                        onclick={() => currentNoteIndex = i}
                                        class="ios-font flex cursor-pointer flex-col justify-center border-b border-gray-300/50 px-4 py-2 hover:bg-yellow-900/5 {currentNoteIndex === i ? 'bg-yellow-900/10' : ''}"
                                    >
                                        <div class="truncate text-base font-bold text-gray-800">{note.title}</div>
                                        <div class="text-xs text-gray-500">{new Date().toLocaleDateString()}</div>
                                    </div>
                                {/each}
                            </div>
                        </div>

                        <div class="flex h-full flex-1 flex-col bg-[#fdf6e3]">
                            <div class="ios-leather flex h-12 shrink-0 items-center justify-between px-3">
                                <div></div> <div class="flex gap-2">
                                    <button class="ios-btn ios-sans text-lg leading-none">Previous Section</button>
                                    <button class="ios-btn ios-sans text-lg leading-none">Next Section</button>
                                </div>
                            </div>

                            <div class="ios-paper h-full flex-1 overflow-y-auto">
                                {#key currentNoteIndex}
                                    <div class="p-8 pl-14">
                                        <div class="ios-font text-gray-800">
                                            <div class="mb-4 text-center text-sm text-gray-400">{new Date().toLocaleDateString()}</div>
                                            <h1 class="mb-4 text-2xl font-bold">{notes[currentNoteIndex].title}</h1>
                                            
                                            <pre contenteditable="true" class="ios-font whitespace-pre-wrap text-lg leading-[32px] text-gray-700 outline-none">{notes[currentNoteIndex].content}</pre>
                                            
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