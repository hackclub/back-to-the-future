<script lang="ts">
    import back from '$lib/assets/w8back.png';

    const windows8colors = [
        { name: 'Orange', hex: '#F09609' },
        { name: 'Yellow', hex: '#FFC40D' },
        { name: 'Dark Orange', hex: '#D24726' },
        { name: 'Red', hex: '#E51400' },
        { name: 'Magenta', hex: '#FF0097' },
        { name: 'Purple', hex: '#A200FF' },
        { name: 'Dark Purple', hex: '#7E3878' },
        { name: 'Blue', hex: '#1BA1E2' },
        { name: 'Dark Blue', hex: '#0020FF' },
        { name: 'Light Blue', hex: '#3399FF' },
        { name: 'Teal', hex: '#00ABA9' },
        { name: 'Light Teal', hex: '#00E3E3' },
        { name: 'Green', hex: '#339933' },
        { name: 'Dark Green', hex: '#008A00' },
        { name: 'Lime', hex: '#8CBF26' },
        { name: 'Brown', hex: '#A05000' },
        { name: 'Pink', hex: '#E671B8' },
        { name: 'Crimson', hex: '#B91D47' },
        { name: 'Steel', hex: '#464646' },
        { name: 'Charcoal', hex: '#2B2B2B' },
        { name: 'Windows Brand Blue', hex: '#2D89EF' },
        { name: 'Xbox Green', hex: '#107C10' },
        { name: 'Office Red', hex: '#D83B01' },
        { name: 'Bing Gold', hex: '#FFB900' },
        { name: 'Desktop Gray', hex: '#6B6B6B' }
    ].map((x) => x.hex);
</script>

<div
    class="flex h-screen w-screen flex-col gap-8 overflow-x-auto p-20 font-extralight"
    style="font-family: 'Segoe UI', sans-serif;"
    style:background-image="url('/windows8start.png')"
>
    <div class="text-5xl text-white">Start (coding)</div>

    <div class="flex flex-row gap-8 overflow-y-hidden overflow-x-auto">
        <div class="flex h-full flex-col flex-wrap items-start justify-start gap-4 text-white *:m-0">
            <div class="flex h-32 w-64 flex-row gap-4">
                <div class="flex-1 p-4" style:background-color={windows8colors[0]}>hi</div>
                <div class="flex-1 p-4" style:background-color={windows8colors[0]}>hi</div>
            </div>

            <div class="h-32 w-64 p-4" style:background-color={windows8colors[0]}>hi</div>

            <div class="flex h-32 w-64 flex-row gap-4">
                <div class="flex-1 p-4" style:background-color={windows8colors[0]}>hi</div>
                <div class="flex-1 p-4" style:background-color={windows8colors[0]}>hi</div>
            </div>

            <div class="h-32 w-64 p-4" style:background-color={windows8colors[0]}>hi</div>
        </div>

        <div class="flex h-full flex-col flex-wrap items-start justify-start gap-4 text-white *:m-0">
            <div class="flex h-32 w-64 flex-row gap-4">
                <div class="flex-1 p-4" style:background-color={windows8colors[0]}>hi</div>
                <div class="flex-1 p-4" style:background-color={windows8colors[0]}>hi</div>
            </div>

            <div class="h-32 w-64 p-4" style:background-color={windows8colors[0]}>hi</div>

            <div class="flex h-32 w-64 flex-row gap-4">
                <div class="flex-1 p-4" style:background-color={windows8colors[0]}>hi</div>
                <div class="flex-1 p-4" style:background-color={windows8colors[0]}>hi</div>
            </div>

            <div class="h-32 w-64 p-4" style:background-color={windows8colors[0]}>hi</div>
        </div>
    </div>
</div>

<style>
    html {
        background-image: url('/windows8start.png');
    }
</style>
