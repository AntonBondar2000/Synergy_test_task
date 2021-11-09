<template>
  <header class="header">
    <h1>Занимаемые должности</h1>
    <div class="header__settings">
      <div class="header__settings__search">
        <input type="text" placeholder="Поиск по сотруднику" v-model="currentSearch">
      </div>
      <div class="header__settings__additional">
        <div class="header__settings__additional__show-fire">
          <input type="checkbox" name="show_fire" id="show_fire" v-model="showFire">
          <label for="show_fire">Показывать уволенные</label>
        </div>
        <div class="header__settings__additional__button-add-remove">
          <button
            :disabled="countCheckedCheckbox < 1"
            class="header__settings__additional__button-add-remove__add"
          >
            {{textButtonAdd}}
          </button>
          <button
            :disabled="countCheckedCheckbox < 1"
            class="header__settings__additional__button-add-remove__remove"
          >
            {{textButtonRemove}}
          </button>
        </div>
      </div>
    </div>
  </header>
  <main>
    <table class="table-occupations">
      <thead>
        <tr>
          <th></th>
          <th>Сотрудник</th>
          <th>Компания</th>
          <th>Должность</th>
          <th>Дата приема</th>
          <th>Дата увольнения</th>
          <th>Ставка</th>
          <th>База</th>
          <th>Аванс</th>
          <th>Почасовая</th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="(item, index) in paginatedData"
          :key="index"
          :class="{ item_dismissed: item.fireDate }"
        >
            <td>
              <input
                type="checkbox"
                v-if="!item.fireDate"
                class="check"
                @change="checkCount()"
              >
            </td>
            <td>{{item.name}}</td>
            <td>{{item.companyName}}</td>
            <td>{{item.positionName}}</td>
            <td>{{item.hireDate}}</td>
            <td>{{item.fireDate}}</td>
            <td style="position: relative; cursor: pointer;" @click="showChangeForm">
              <p v-if="!item.fireDate">
                {{item.salary}}({{item.fraction}}%)
              </p>
              <p v-else>-</p>
              <div v-if="!item.fireDate" class="change_salary form-change">
                <div class="input-inline">
                  <label for="salary">Salary</label>
                  <input type="text" id='salary'>
                </div>
                <div class="input-inline">
                  <label for="fraction">Fraction</label>
                   <input type="text" id="fraction">
                </div>
                <div class="form-change__buttons">
                  <button @click="closeChangeForm">
                    Закрыть
                  </button>
                  <button @click="updateOccupationMultiply($event, item.id, 'salary', 'fraction')">
                    Сохранить
                  </button>
                </div>
              </div>
            </td>
            <td style="position: relative; cursor: pointer;" @click="showChangeForm">
              <p>{{!item.fireDate ? item.base: '-'}}</p>
              <div v-if="!item.fireDate" class="change_salary form-change">
                <div class="input-inline">
                  <label for="base">Base</label>
                  <input class="input-change-data" type="text" id='base'>
                </div>
                <div class="form-change__buttons">
                  <button @click="closeChangeForm">
                    Закрыть
                  </button>
                  <button @click="updateOccupationSimple($event, item.id, 'base', false)">
                    Сохранить
                  </button>
                </div>
              </div>
            </td>
            <td style="position: relative; cursor: pointer;" @click="showChangeForm">
              <p>{{!item.fireDate ? item.advance: '-'}}</p>
              <div v-if="!item.fireDate" class="change_salary form-change">
                <div class="input-inline">
                  <label for="advance">Advance</label>
                  <input class="input-change-data" type="text" id='advance'>
                </div>
                <div class="form-change__buttons">
                  <button @click="closeChangeForm">
                    Закрыть
                  </button>
                  <button @click="updateOccupationSimple($event, item.id, 'advance', false)">
                    Сохранить
                  </button>
                </div>
              </div>
            </td>
            <td style="position: relative;" @click="showChangeForm">
              <input
                v-if="!item.fireDate"
                type="checkbox"
                :checked="item.byHours"
                @change="updateOccupationSimple($event, item.id, 'byHours', true)"
              >
              <p v-else>-</p>
            </td>
        </tr>
    </tbody>
    </table>
    <div class="pagination">
      <div class="pagination__current-page">Всего страниц: {{pageCount}}</div>
      <button @click="prevPage" class="pagination__button" :disabled="hasPrev">Предыдущая</button>
      <div class="pagination__current-page">{{pageNumber + 1}}</div>
      <button @click="nextPage" class="pagination__button" :disabled="hasNext">Следующая</button>
    </div>
  </main>
</template>

<script>

import axios from 'axios'
export default {
  name: 'HomePage',
  data () {
    return {
      allOccupations: [],
      pageNumber: 0,
      paginationSize: 2,
      currentSearch: '',
      showFire: false,
      countCheckedCheckbox: 0
    }
  },
  methods: {
    updateOccupationSimple (e, id, key, flagCheckbox) {
      const elem = this.allOccupations.filter(item => item.id === id)[0]
      let value = []
      if (flagCheckbox) {
        value = e.target.checked
      } else {
        value = e.target.parentNode.parentNode.querySelector('input').value
      }
      elem[key] = value
      axios({
        method: 'POST',
        url: 'http://0.0.0.0:8081/occupation/api',
        data: {
          query: `
                    mutation updateOccupation{
                      updateOccupation(
                      id:${elem.id},
                      name:"${elem.name}",
                      companyName:"${elem.companyName}",
                      positionName:"${elem.positionName}",
                      hireDate:"${elem.hireDate}",
                      salary:${elem.salary},
                      fraction:${elem.fraction},
                      base:${elem.base},
                      advance:${elem.advance},
                      byHours:${elem.byHours}
                      ) {
                          occupation{
                            id,
                          }
                      }
                }`
        }
      }).then(response => {
        console.log('worked')
      })
    },
    updateOccupationMultiply (e, id, key, key2) {
      const elem = this.allOccupations.filter(item => item.id === id)[0]
      console.log(e.target.parentNode)
      const value1 = e.target.parentNode.parentNode.parentNode.querySelector('input#salary').value
      const value2 = e.target.parentNode.parentNode.parentNode.querySelector('input#fraction').value
      elem[key] = value1
      elem[key2] = value2
      axios({
        method: 'POST',
        url: 'http://0.0.0.0:8081/occupation/api',
        data: {
          query: `
                    mutation updateOccupation{
                      updateOccupation(
                      id:${elem.id},
                      name:"${elem.name}",
                      companyName:"${elem.companyName}",
                      positionName:"${elem.positionName}",
                      hireDate:"${elem.hireDate}",
                      salary:${elem.salary},
                      fraction:${elem.fraction},
                      base:${elem.base},
                      advance:${elem.advance},
                      byHours:${elem.byHours}
                      ) {
                          occupation{
                            id,
                          }
                      }
                }`
        }
      }).then(response => {
        console.log(response)
      })
    },
    nextPage () {
      this.pageNumber++
    },
    prevPage () {
      this.pageNumber--
    },
    checkCount () {
      const selectedCheckBoxes = document.querySelectorAll('.check:checked')
      this.countCheckedCheckbox = selectedCheckBoxes.length
    },
    showChangeForm (e) {
      e.target.querySelector('.form-change').style.display = 'block'
    },
    closeChangeForm (e) {
      e.target.parentNode.parentNode.style.display = 'none'
    },
    getAllOccupations () {
      axios({
        method: 'POST',
        url: 'http://0.0.0.0:8081/occupation/api',
        data: {
          query: `
                    {
                      getOccupations {
                        id,
                        name,
                        companyName,
                        positionName,
                        hireDate,
                        fireDate,
                        salary,
                        fraction,
                        base,
                        advance,
                        byHours
                      }
                    }`
        }
      }).then(response => {
        this.allOccupations = response.data.data.getOccupations
      })
    }
  },
  computed: {
    textButtonAdd () {
      if (this.countCheckedCheckbox > 1) { return 'Принять на должности' }
      return 'Принять на должность'
    },
    textButtonRemove () {
      if (this.countCheckedCheckbox > 1) { return 'Снять с должностей' }
      return 'Снять с должности'
    },
    hasNext () {
      return this.pageNumber === this.pageCount - 1 || this.pageCount === 0
    },
    hasPrev () {
      return this.pageNumber === 0
    },
    pageCount () {
      return Math.ceil(this.filterData.length / this.paginationSize)
    },
    paginatedData () {
      const start = this.pageNumber * this.paginationSize
      const end = start + this.paginationSize
      return this.filterData.slice(start, end)
    },
    filterData () {
      // eslint-disable-next-line vue/no-side-effects-in-computed-properties
      this.pageNumber = 0
      return this.allOccupations.filter(
        item => item.name.toLowerCase().indexOf(this.currentSearch.toLowerCase()) !== -1
      ).filter(item => !this.showFire ? Boolean(item.fireDate) === false : true)
    }
  },
  mounted () {
    this.getAllOccupations()
  }
}
</script>

<style scoped lang="scss">
  .header{
    width: 85%;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    margin-top: 50px;
    &__settings{
      &__search{
        width: 100%;
        min-width: 200px;
        input{
          width: 100%;
          padding: 5px 15px;
          outline: none;
          border: 1px solid #a7a2a2;
          border-radius: 10px;
          font-paginationSize: 18px;
        }
      }
      &__additional{
        display: flex;
        margin-top: 25px;
        align-items: center;
        &__show-fire{
          label{
            font-paginationSize: 18px;
            margin-left: 15px;
            cursor: pointer;
          }
          input{
            transform:scale(1.2);
            cursor:pointer;
          }
        }
        &__button-add-remove{
          margin-left: 25px;
          button{
            font-paginationSize: 16px;
            padding: 5px 15px;
            border: none;
            transition-duration: .1s;
            &:not(:disabled){
              &:hover{
                box-shadow: black 1px 1px 5px;
              }
              cursor: pointer;
            }
          }
          &__add{
            background-color: rgb(137, 216, 137);
          }
          &__remove{
            background-color: rgb(204, 104, 104);
            margin-left: 25px;
          }
        }
      }
    }
  }
main{
  .table-occupations{
    width: 100%;
    border-spacing: 0px;
    border-collapse: collapse;
    .item_dismissed{
      background-color: rgb(235, 104, 104);
      width: 100%;
    }
  }
}
main{
  width: 85%;
  margin: 0 auto;
  margin-top: 50px;
  .table-occupations{
    width: 100%;
    border-spacing: 0px;
    border-collapse: collapse;
    .item_dismissed{
      background-color: rgb(235, 104, 104);
    }
    td, th{
      padding: 15px 20px;
      p{
        pointer-events: none;
      }
    }
    th{
      text-align: left;
      border-bottom: 1px solid #c6c6c6;
    }
    .form-change{
      padding: 25px 50px;
      border: 1px solid #c6c6c6;
      position: absolute;
      top: 100%;
      left: -50%;
      display: none;
      background: white;
      z-index: 1000;
      .input-inline{
        display: flex;
        width: 350px;
        justify-content: space-between;
        align-items: center;
        &:not(:first-child){
          margin-top: 15px;
        }
        input{
          font-paginationSize: 16px;
          padding: 5px 15px;
          outline: none;
          border: 1px solid #a7a2a2;
          border-radius: 10px;
        }
        label{
          font-paginationSize: 16px;
        }
      }
      &__buttons{
        margin-top: 20px;
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        button{
          font-paginationSize: 16px;
          padding: 7px 15px;
          border: none;
          transition-duration: .1s;
          &:hover{
            box-shadow: black 1px 1px 5px;
          }
          cursor: pointer;
          }
        }
      }
    }
  .pagination{
    display: flex;
    width: 100%;
    justify-content: flex-end;
    align-items: center;
    margin-top: 50px;
    &__button{
      width: 15%;
      font-paginationSize: 16px;
      padding: 7px 15px;
      border: none;
      transition-duration: .1s;
      &:not(:disabled){
        &:hover{
          box-shadow: black 1px 1px 5px;
        }
        cursor: pointer;
      }
    }
    &__current-page{
      padding: 0 10px;
      font-paginationSize: 18px;
    }
  }
}
</style>
