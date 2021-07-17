<template>
  <router-view />
</template>

<script>
import { createNamespacedHelpers } from "vuex";

const { mapMutations } = createNamespacedHelpers("auth");

export default {
  name: "App",
  methods: {
    ...mapMutations(["initialize"]),
  },
  created() {
    this.initialize();
  },
};
</script>
