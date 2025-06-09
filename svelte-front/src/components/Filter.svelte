<script>
  export let columns;

  let columnOptions = columns.filter(c => c.sortable);
  let selectedColumn = columnOptions[0]?.key;
  let condition = 'contains';
  let value = '';

  const conditions = [
    { value: 'contains', label: 'Содержит' },
    { value: 'equals', label: 'Равно' },
    { value: 'gt', label: 'Больше' },
    { value: 'lt', label: 'Меньше' }
  ];

  const handleSubmit = () => {
    if (!value) return;

    const filter = {};
    filter[`${selectedColumn}__${condition}`] = value;
    dispatch('filter', filter);
  };

  const handleReset = () => {
    selectedColumn = columnOptions[0]?.key;
    condition = 'contains';
    value = '';
    dispatch('filter', {});
  };
</script>

<div class="filter-container">
  <select bind:value={selectedColumn}>
    {#each columnOptions as column}
      <option value={column.key}>{column.label}</option>
    {/each}
  </select>

  <select bind:value={condition}>
    {#each conditions as cond}
      <option value={cond.value}>{cond.label}</option>
    {/each}
  </select>

  <input
    type="text"
    bind:value={value}
    placeholder="Значение для фильтрации"
  />

  <button on:click={handleSubmit}>Применить</button>
  <button on:click={handleReset}>Сбросить</button>
</div>

<style>
  .filter-container {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
    flex-wrap: wrap;
    align-items: center;
  }

  select, input {
    padding: 8px 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
  }

  button {
    padding: 8px 16px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background-color: #0056b3;
  }
</style>