<template>
  <Navbar />
  <div class="bg">
    <v-container>
      <v-row align-content="center" style="height: 900px">
        <v-col align="center" class="text-white">
          <h1 class="text-h1 font-weight-medium">Vendeye</h1>
          <p class="text-h5 font-weight-medium mt-8">
            Search vending machines on fly!
          </p>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import Navbar from "./Navbar.vue";

export default {
  components: {
    Navbar,
  },
};
</script>

<style lang="scss" scoped>
.bg {
  background-image: url("../background.jpg");
  background-size: cover;
  background-position: center;
}
</style>
