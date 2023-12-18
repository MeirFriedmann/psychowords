<script>
    let message = '';

    async function fetchData() {
        const response = await fetch('http://localhost:5000');
        const data = await response.json();
        message = data.message;
    }
</script>

<main>
    <h1>Svelte + Flask Example</h1>
    <button on:click={fetchData}>Fetch Data</button>
    {#if message}
        <p>{message}</p>
    {/if}
</main>

<style>
    main {
        text-align: center;
        margin: 2em;
    }

    button {
        padding: 0.5em;
        margin: 1em;
    }
</style>

