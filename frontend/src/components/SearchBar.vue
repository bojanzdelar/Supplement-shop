<template>
  <div
    class="offcanvas offcanvas-top"
    tabindex="-1"
    id="searchBar"
    aria-labelledby="searchBarLabel"
  >
    <div class="offcanvas-header mt-2">
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
        <div class="input-group">
          <input
            v-model="query"
            type="text"
            class="form-control"
            placeholder="Search for products, brands and more"
            aria-label="Query"
          />
          <span class="input-group-text">
            <button
              class="btn"
              type="submit"
              data-bs-dismiss="offcanvas"
              aria-label="Search"
            >
              <i class="bi bi-search"></i>
            </button>
          </span>
        </div>
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
      this.$router.push(`/search?q=${query}`);
    },
  },
};
</script>

<style scoped>
.offcanvas-top {
  height: 20vh;
}
</style>
