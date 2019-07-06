<template>
    <div class="row">
      <div class="col-12">
        <card :title="table1.title" :subTitle="table1.subTitle">
          <div slot="raw-content" class="table-responsive">
            <paper-table :data="table1.data" :columns="table1.columns">

            </paper-table>
          </div>
        </card>
      </div>


    </div>
</template>
<script>
import { PaperTable } from "@/components";
import $ from 'jquery';

export default {
  components: {
    PaperTable
  },
  data() {
    return {
      table1: {
        title: "BTC 交易记录",
        subTitle: "",
        columns: ["Id", "price", "volume", "dealTime"],
        data: []
      }
    };
  },

  mounted(){
    this.getTableLists();
  },

  methods: {

    getTableLists: function () {
      let self = this;
      $.ajax({
        url: 'http://127.0.0.1:5000/api/chartsList',
        type: 'GET',
        success: function (res) {
          let newData = [];
          for(let i in res.data){
            newData[i] = {
              Id: res.data[i]['id']
              ,price: res.data[i]['price']
              ,volume: res.data[i]['volume']
              ,dealTime: res.data[i]['dealTime']
            }
          }
          self.table1.data = newData;
        }
      });
    }
  }

};
</script>
<style>
</style>
