<template>
    <div class="records">
      <router-view></router-view>
      <div class="appointTable">
      <br />
      <br />
      <h3>门诊预约信息</h3>
      <table>
        <thead>
          <tr>
            <th>预约时间</th>
            <th>科室名称</th>
            <th>医生姓名</th>
            <th>是否完成</th>
            <th>操作</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="appointment in appointments" :key="appointment.time" :class="{ 'finished': appointment.isFinished, 'unfinished': !appointment.isFinished }">
            <td>{{ appointment.time }}</td>
            <td>{{ appointment.department }}</td>
            <td>{{ appointment.doctor }}</td>
            <td>
              {{ appointment.isFinished ? '已完成' : '未完成' }}
            </td>
            <td>
              <span v-if="!appointment.isFinished" class="cancel" @click="showCancelDialog(appointment)">取消预约</span></td>
          </tr>
        </tbody>
      </table>
      </div>

      <div v-if="showDialog" class="dialog">
        <p>您确定要取消时间为 {{ selectedAppointment.time }} 的预约吗？</p>
        <div class="buttons">
          <button @click="cancelAppointment">确定</button>
          <button @click="hideCancelDialog">取消</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Appointment',
    data() {
      return {
        appointments: [
          {'time': '2023-06-01 9:00', 'department': '内科', 'doctor': '张三', 'isFinished': true},
          {'time': '2023-07-01 10:00', 'department': '外科', 'doctor': '王五', 'isFinished': false}
        ],
        selectedAppointment: null,
        showDialog: false
      }
    },
    methods: {
      showCancelDialog(appointment) {
        this.selectedAppointment = appointment;
        this.showDialog = true;
      },
      hideCancelDialog() {
        this.selectedAppointment = null;
        this.showDialog = false;
      },
      cancelAppointment() {
        console.log('时间为' + this.selectedAppointment.time + '的预约已取消预约。');
        alert('时间为 ' + this.selectedAppointment.time + ' 的预约已取消预约。');
        this.selectedAppointment.isBooked = false;
        this.hideCancelDialog();
      }
    }
  };
  </script>
  
  <style scoped>
  .appointment {
    display: flex;
  }
  .finished {
    background-color: #FFFFFF;
  }
  .unfinished {
    background-color: #DDFFDD;
  }
  .cancel {
    color: blue;
    text-decoration: underline;
    cursor: pointer;
  }
  .dialog {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    padding: 20px;
    background-color: white;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5);
  }
  .buttons {
    margin-top: 20px;
    text-align: right;
  }
  </style>
