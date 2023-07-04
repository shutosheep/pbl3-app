<template>
  <h2>Vending machine Info</h2>
  <div v-if="menu">
    <div class="menu">
      <h3>Menu</h3>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Price</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="i in menu">
            <td>{{ i.name }}</td>
            <td>{{ i.price }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    menu: { },
    location: { },
  },
}
</script>

<style lang="scss" scoped>
</style>