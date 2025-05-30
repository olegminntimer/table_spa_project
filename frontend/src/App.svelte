<script>
  import Table from './Table.svelte';
</script>

<main>
  <h1>Таблица данных</h1>
  <Table />
</main>

<style>
  main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
    font-family: Arial, sans-serif;
  }

  h1 {
    text-align: center;
    margin-bottom: 30px;
    color: #333;
  }
</style>
<style global>
  @import 'bootstrap/dist/css/bootstrap.min.css';
</style>