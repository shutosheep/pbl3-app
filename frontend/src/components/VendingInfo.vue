<template>
  <div v-if="menu">
    <div class="menu">
      <h2>Menu</h2>
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
  },
}
</script>

<style lang="scss" scoped>
</style>