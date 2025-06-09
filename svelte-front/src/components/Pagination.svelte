<script>
  export let current;
  export let total;
  export let perPage;

  $: totalPages = Math.ceil(total / perPage);
  $: pages = Array.from({ length: Math.min(totalPages, 5) }, (_, i) => {
    let start = Math.max(1, current - 2);
    start = Math.min(start, totalPages - 4);
    return start + i;
  });

  const handlePageChange = (page) => {
    if (page >= 1 && page <= totalPages && page !== current) {
      dispatch('pageChange', page);
    }
  };
</script>

<div class="pagination">
  <button
    on:click={() => handlePageChange(1)}
    disabled={current === 1}
  >«</button>

  <button
    on:click={() => handlePageChange(current - 1)}
    disabled={current === 1}
  >‹</button>

  {#each pages as page}
    <button
      class={current === page ? 'active' : ''}
      on:click={() => handlePageChange(page)}
    >{page}</button>
  {/each}

  <button
    on:click={() => handlePageChange(current + 1)}
    disabled={current === totalPages}
  >›</button>

  <button
    on:click={() => handlePageChange(totalPages)}
    disabled={current === totalPages}
  >»</button>
</div>

<style>
  .pagination {
    display: flex;
    gap: 5px;
    justify-content: center;
    margin-top: 20px;
  }

  .pagination button {
    padding: 5px 10px;
    border: 1px solid #ddd;
    background: white;
    cursor: pointer;
  }

  .pagination button.active {
    background-color: #007bff;
    color: white;
    border-color: #007bff;
  }

  .pagination button:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
</style>