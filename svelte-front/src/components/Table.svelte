<script>
  import { onMount } from 'svelte';
  import axios from 'axios';
  import Filter from './Filter.svelte';
  import Pagination from './Pagination.svelte';

  export let data = [];
  export let columns = [
    { key: 'date', label: 'Дата' },
    { key: 'name', label: 'Название', sortable: true },
    { key: 'quantity', label: 'Количество', sortable: true },
    { key: 'distance', label: 'Расстояние', sortable: true }
  ];

  let loading = false;
  let totalItems = 0;
  let currentPage = 1;
  let itemsPerPage = 10;
  let sortField = 'name';
  let sortDirection = 'asc';
  let filters = {};

  const fetchData = async () => {
    loading = true;
    try {
      const params = {
        page: currentPage,
        page_size: itemsPerPage,
        ordering: `${sortDirection === 'desc' ? '-' : ''}${sortField}`,
        ...filters
      };

      const response = await axios.get('/items/', { params });
      data = response.data.results;
      totalItems = response.data.count;
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      loading = false;
    }
  };

  const handleSort = (field) => {
    if (sortField === field) {
      sortDirection = sortDirection === 'asc' ? 'desc' : 'asc';
    } else {
      sortField = field;
      sortDirection = 'asc';
    }
    fetchData();
  };

  const handleFilter = (newFilters) => {
    filters = newFilters;
    currentPage = 1;
    fetchData();
  };

  const handlePageChange = (page) => {
    currentPage = page;
    fetchData();
  };

  onMount(fetchData);
</script>

<div class="table-container">
  <Filter on:filter={handleFilter} {columns} />

  {#if loading}
    <div class="spinner">Loading...</div>
  {:else}
    <table class="table table-striped">
      <thead>
        <tr>
          {#each columns as column}
            <th>
              {column.label}
              {#if column.sortable}
                <button
                  class="sort-btn {sortField === column.key ? 'active' : ''}"
                  on:click={() => handleSort(column.key)}
                >
                  {sortField === column.key && sortDirection === 'asc' ? '↑' : '↓'}
                </button>
              {/if}
            </th>
          {/each}
        </tr>
      </thead>
      <tbody>
        {#each data as item (item.id)}
          <tr>
            <td>{new Date(item.date).toLocaleDateString()}</td>
            <td>{item.name}</td>
            <td>{item.quantity}</td>
            <td>{item.distance}</td>
          </tr>
        {:else}
          <tr>
            <td colspan={columns.length}>No data available</td>
          </tr>
        {/each}
      </tbody>
    </table>

    <Pagination
      current={currentPage}
      total={totalItems}
      perPage={itemsPerPage}
      onPageChange={handlePageChange}
    />
  {/if}
</div>

<style>
  .table-container {
    margin: 20px;
    overflow-x: auto;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
  }

  th, td {
    padding: 12px 15px;
    text-align: left;
    border-bottom: 1px solid #ddd;
  }

  th {
    background-color: #f8f9fa;
    position: sticky;
    top: 0;
  }

  .sort-btn {
    background: none;
    border: none;
    cursor: pointer;
    margin-left: 5px;
  }

  .sort-btn.active {
    color: #007bff;
  }

  .spinner {
    text-align: center;
    padding: 20px;
  }
</style>