<template>
  <div v-if="menu">
    <div class="menu">
      <h2 class="text-h4 my-3">Menu</h2>
      <v-table density="compact">
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="i in menu">
            <td>
              <span
                class="red"
                v-if="
                  (filterType == filterTypeOptions[0] &&
                    filterValue == i.name) ||
                  (filterType == filterTypeOptions[1] && filterValue >= i.price)
                "
              >
                {{ i.name }}
              </span>
              <span v-else>
                {{ i.name }}
              </span>
            </td>
            <td>
              <span
                class="red"
                v-if="
                  (filterType == filterTypeOptions[0] &&
                    filterValue == i.name) ||
                  (filterType == filterTypeOptions[1] && filterValue >= i.price)
                "
              >
                {{ i.price }}
              </span>
              <span v-else>
                {{ i.price }}
              </span>
            </td>
          </tr>
        </tbody>
      </v-table>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    menu: {},
    filterType: {},
    filterTypeOptions: {},
    filterValue: {},
  },
};
</script>

<style lang="scss" scoped>
.red {
  color: red;
}
</style>
