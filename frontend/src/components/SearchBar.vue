<template>
  <div
    class="offcanvas offcanvas-top"
    tabindex="-1"
    id="searchBar"
    aria-labelledby="searchBarLabel"
  >
    <div class="offcanvas-header">
      <h5 id="searchBarLabel">What are you looking for?</h5>
      <button
        type="button"
        class="btn-close text-reset"
        data-bs-dismiss="offcanvas"
        aria-label="Close"
      ></button>
    </div>
    <div class="offcanvas-body">
      <form @submit.prevent="search(query)">
        <input
          v-model="query"
          type="text"
          class="form-control"
          placeholder="Search for products, brands and more"
          aria-label="Query"
        />
        <input
          class="btn btn-outline-success"
          type="submit"
          value="Search"
          data-bs-dismiss="offcanvas"
          arial-label="Search"
        />
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name: "SearchBar",
  data() {
    return {
      query: "",
    };
  },
  methods: {
    search(query) {
      this.$router.push(`/search/?q=${query}`);
    },
  },
};
</script>