Vue.component('grid-itens', {
    template:
    `
<div>
  <h3 class="card-title">Selecione:</h3>  
  <div v-for="(linha, pos_x) of localGridData" class="row" style="margin-bottom:0; margin-left:30px">
    <div v-for="(valor, pos_y) of linha" class="col" v-bind:style="{width: opt.boxSizeW + 'px', height:opt.boxSizeH + 'px'}" style="margin:0; padding:0">
      <div v-on:click="trocaValor(pos_x, pos_y)" v-bind:style="{width: opt.boxSizeW + 'px', height:opt.boxSizeH + 'px'}" style="border: 1px solid #ccc; padding: 6px "  :class="pontoSelecionado(valor)">
      </div>
    </div>
  </div>
  
  <h3 class="card-title">Saida json:</h3>
  <textarea rows="3">{{saidaJson}}</textarea>
</div>
`,
    props: {
        gridData: null,
        scale: null,
        opt: null
    },
    data: function() {
        return {
            output: '',
            localGridData: [
                [] = ';'
            ]
        }
    },
    created: function() {
        this.localGridData = this.gridData;
    },
    methods: {
        trocaValor: function(pos_x, pos_y) {
            let valor = this.localGridData[pos_x][pos_y].value;
            
            const newRow = this.localGridData[pos_x].slice(0)
            
            if (valor < 10) {
                newRow[pos_y].value = parseInt(valor) + 1;
            } else {
                newRow[pos_y].value = 0;
            }
            
            this.$set(this.localGridData, pos_x, newRow);
        },
        pontoSelecionado: function(valor) {
            return this.scale[valor.value];
        }
    },
    watch: {
        gridData: function() {
            this.localGridData = this.gridData;
        }
    },
    computed: {
        saidaJson: function() {
            return JSON.stringify(this.localGridData);
        }
    },
});
