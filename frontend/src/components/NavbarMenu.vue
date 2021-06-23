<template>
  <div
    class="offcanvas offcanvas-start"
    tabindex="-1"
    id="navbarMenu"
    aria-labelledby="navbarMenu"
  >
    <div class="offcanvas-header">
      <h5 class="offcanvas-title" id="navbarMenuLabel">Close menu</h5>
      <button
        type="button"
        class="btn-close text-reset"
        data-bs-dismiss="offcanvas"
        aria-label="Close"
      ></button>
    </div>
    <div class="offcanvas-body">
      <ul class="list-group list-group-root list-unstyled">
        <li>
          <div
            data-bs-toggle="collapse"
            data-bs-target="#collapseCategories"
            class="list-group-item list-group-item-action text-uppercase"
          >
            Shop
          </div>
          <ul class="collapse list-group list-unstyled" id="collapseCategories">
            <li>
              <router-link
                to="/category/all"
                data-bs-dismiss="offcanvas"
                class="
                  list-group-item list-group-item-action
                  bg-light
                  text-uppercase
                "
                >All Products</router-link
              >
            </li>

            <li v-for="category in categories" :key="category.id">
              <router-link
                :to="{
                  name: 'Category',
                  params: { id: category.id },
                }"
                data-bs-dismiss="offcanvas"
                class="
                  list-group-item list-group-item-action
                  bg-light
                  text-uppercase
                "
              >
                {{ category.name }}
              </router-link>
            </li>
          </ul>
        </li>

        <li>
          <router-link
            to="/about"
            data-bs-dismiss="offcanvas"
            class="list-group-item list-group-item-action text-uppercase"
          >
            About
          </router-link>
        </li>

        <li>
          <router-link
            to="/about"
            class="list-group-item list-group-item-action text-uppercase"
          >
            Contact
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "NavbarMenu",
  props: {
    categories: Array,
  },
};
</script>

<style scoped>
.list-group.list-group-root .list-group .list-group-item {
  padding-left: 30px;
}
</style>