<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <Button type="success" @click="ledon">开灯</Button>
    <Button type="warning" @click="ledoff">关灯</Button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: '这是测试'
    }
  },
  methods: {
    ledon () {
      axios.get('http://192.168.2.167:8000/led/on/')
        .then(
          (res) => {
            console.log(res.data)
          }
        )
        .catch()
    },
    ledoff () {
      axios.get('http://192.168.2.167:8000/led/off/')
        .then(
          (res) => {
            console.log(res.data)
          }
        )
        .catch()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
