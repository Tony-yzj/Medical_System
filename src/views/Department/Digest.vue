<template>
  <div>
    <div class="department">
      <h2 class="title">消化内科</h2>
      <p class="description">消化内科专注于胃肠道疾病的诊断和治疗。</p>
    </div>

    <div class="schedule">
      <table>
        <thead>
          <tr>
            <th></th>
            <th v-for="timeSlot in timeSlots" :key="timeSlot">{{ timeSlot }}</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(day, dayIndex) in days" :key="day">
            <td>{{ day }}</td>
            <td
              v-for="(available, timeIndex) in getTimeSlotsAvailability(dayIndex)"
              :key="timeIndex"
              :class="{
                'time-slot': true,
                'available': (getBusyStatus(dayIndex, timeIndex) == 0),
                'half-booked':(getBusyStatus(dayIndex, timeIndex) == 2),
                'booked': (getBusyStatus(dayIndex, timeIndex) == 1),
                'gray': !isAvailable(dayIndex, timeIndex)
              }"
              @click="book(dayIndex, timeIndex)"
            >
              <span v-if="available">{{ getDoctorsAvailability(dayIndex, timeIndex) }}</span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- <div v-if="selectedDoctor" class="doctor-intro">
      <h3>医生简介</h3>
      <p class="doctor-name">{{ selectedDoctor.name }}</p>
      <p class="doctor-title">{{ selectedDoctor.title }}</p>
      <p>{{ selectedDoctor.introduction }}</p>
    </div> -->
    <div class="doctor">
        <h3>本周门诊医生介绍</h3>
        <ul v-for="(item, index) in doctors" :key="index">
          <li>{{ item.name }}:{{ item.title }},{{ item.introduction }}</li>
        </ul>
      </div>

    <div v-if="dialogVisible" class="dialog-overlay">
      <div class="dialog-box">
        <h3>预约确认</h3>
        <p>请选择医生：</p>
        <select v-model="selectedDoctor" class="doctor-select">
          <option v-for="doctor in getAvailableDoctors(selectedDay, selectedTimeSlot)" :key="doctor.name">
            {{ doctor.name }}
          </option>
        </select>
        <div class="button-group">
          <button class="cancel-button" @click="cancelBooking">取消</button>
          <button class="confirm-button" @click="confirmBooking">确认预约</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      days: ['周一', '周二', '周三', '周四', '周五'],
      timeSlots: [
        '8:00-9:00',
        '9:00-10:00',
        '10:00-11:00',
        '13:00-14:00',
        '14:00-15:00',
        '15:00-16:00',
        '16:00-17:00'
      ],
      schedule: [
        [true, false, true, false, true, true, true],
        [true, true, true, true, false, true, true],
        [false, false, true, true, true, false, true],
        [true, true, false, false, false, true, true],
        [true, true, true, true, true, true, false]
      ],
      doctors: [
        {
          name: '张三',
          title: '主任医师',
          introduction: '张三是消化内科的主任医师，拥有丰富的临床经验。',
          schedule:[
          [false, false, true, false, true, true, true],
          [true, true, true, false, false, true, true],
          [true, false, true, false, true, false, true],
          [true, true, false, false, false, true, true],
          [true, false, true, true, false, true, false]
        ],
        book:[
          [false, false, false, false, false, false, false],
          [false, false, true, false, false, false, true],
          [false, false, false, false, false, false, false],
          [false, false, false, false, false, false, false],
          [false, false, false, false, false, true, false]
        ]
        },
        {
          name: '李四',
          title: '副主任医师',
          introduction: '李四是消化内科的副主任医师，擅长胃肠道疾病的治疗。',
          schedule:[
          [true, false, true, false, true, true, true],
          [true, true, true, true, false, true, true],
          [false, false, true, true, true, false, true],
          [true, true, false, false, false, true, true],
          [true, true, true, true, true, true, false]
        ],
        book:[
          [false, false, false, false, false, false, false],
          [false, false, false, false, false, false, true],
          [false, false, false, false, false, false, false],
          [false, false, false, false, false, false, false],
          [false, false, false, false, false, false, false]
        ]
        }
      ],
      selectedDay: null,
      selectedTimeSlot: null,
      selectedDoctor: null,
      dialogVisible: false
    };
  },
  methods: {
    getTimeSlotsAvailability(dayIndex) {
      this.refreshSchedule(dayIndex);
      return this.schedule[dayIndex];
    },
    refreshSchedule(dayIndex){
      for(var index = 0; index < 7; index=index+1){
        this.schedule[dayIndex][index] = false;
        this.doctors.forEach(doctor => {
          if (this.isdoctorAvailable(doctor, dayIndex, index)) {
            this.schedule[dayIndex][index] = true;
          }
        });
      }
    },
    isAvailable(dayIndex, timeIndex) {
      return this.schedule[dayIndex][timeIndex];
    },
    isdoctorAvailable(doctor, dayIndex, timeIndex) {
      return doctor.schedule[dayIndex][timeIndex];
    },
    isdoctorBusy(doctor, dayIndex, timeIndex) {
      return doctor.book[dayIndex][timeIndex];
    },
    getDoctorsAvailability(dayIndex, timeIndex) {
      const availableDoctors = [];
      this.doctors.forEach(doctor => {
        if (this.isdoctorAvailable(doctor, dayIndex, timeIndex)) {
          availableDoctors.push(doctor.name);
        }
      });
      return availableDoctors.join(', ');
    },
    getAvailableDoctors(dayIndex, timeIndex) {
      const availableDoctors = [];
      this.doctors.forEach(doctor => {
        if (this.isdoctorAvailable(doctor, dayIndex, timeIndex)) {
          availableDoctors.push(doctor);
        }
      });
      return availableDoctors;
    },
    getFreeDoctor(dayIndex, timeIndex) {
      const availableDoctors = [];
      this.doctors.forEach(doctor => {
        if (this.isdoctorAvailable(doctor, dayIndex, timeIndex) && !this.isdoctorBusy(doctor, dayIndex, timeIndex)) {
          availableDoctors.push(doctor);
        }
      });
      return availableDoctors;
    },
    getBusyStatus(dayIndex, timeIndex) {
      const availableDoctors = this.getAvailableDoctors(dayIndex, timeIndex);
      let cnt = 0;
      let free = 0;
      availableDoctors.forEach(doctor => {
        if (!doctor.book[dayIndex][timeIndex]) {
          free++;
        }
        cnt++;
      });
      if (cnt === 0) {
        return -1; // 没有可用的医生
      } else if (free === cnt) {
        return 0; // 所有医生都可用
      } else if (free === 0) {
        return 1; // 所有医生都已预约
      } else {
        return 2; // 部分医生可用
      }
    },
    book(dayIndex, timeIndex) {
      if (this.getBusyStatus(dayIndex, timeIndex) == 0 || this.getBusyStatus(dayIndex, timeIndex) == 2) {
        this.selectedDay = dayIndex;
        this.selectedTimeSlot = timeIndex;
        this.dialogVisible = true;
      }
    },
    cancelBooking() {
      this.selectedDay = null;
      this.selectedTimeSlot = null;
      this.selectedDoctor = null;
      this.dialogVisible = false;
    },
    confirmBooking() {
      if (this.selectedDoctor) {
        const selectedDoctor = this.selectedDoctor;
        const selectedDay = this.selectedDay;
        const selectedTimeSlot = this.selectedTimeSlot;
        var flag = 1;
        // 修改预约时间
        // selectedDoctor.book[selectedDay][selectedTimeSlot] = true;
        const availableDoctors = this.getAvailableDoctors(selectedDay, selectedTimeSlot);
        availableDoctors.forEach(doctor => {
          if (doctor.name == selectedDoctor) {
            if(doctor.book[selectedDay][selectedTimeSlot] == true)
            {
              flag = 0;
            }
            doctor.book[selectedDay][selectedTimeSlot] = true;
          }
        });

        // 清空选中的医生
        this.selectedDoctor = null;

        if(flag)
        {
          console.log('预约成功！');
          this.$message.success('预约成功');
          this.dialogVisible = false;
        }
        else
        {
          console.log('预约失败');
          this.$message.error('预约失败，该医生已被预约');
          this.dialogVisible = false;
        }
      } else {
        console.log('请选择医生');
        this.$message.warning('请选择医生');
      }
    }
  }
};
</script>

<style>
.schedule {
  margin-top: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  text-align: center;
  padding: 10px;
  border: 1px solid #ccc;
}

th {
  background-color: #f0f0f0;
}

.time-slot {
  position: relative;
  cursor: pointer;
}

.available {
  background-color: green;
  color: white;
}

.booked {
  background-color: red;
  color: white;
  cursor: not-allowed;
}

.half-booked {
  background-color: rgb(246, 165, 14);
  color: white;
}

.gray {
  background-color: #f0f0f0;
  cursor: not-allowed;
}

.doctor-intro {
  margin-top: 20px;
}

.doctor-name {
  font-weight: bold;
}

.doctor-title {
  margin-top: 5px;
  color: #666;
}

.dialog-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.dialog-box {
  background-color: white;
  padding: 20px;
  border-radius: 5px;
  width: 300px;
  text-align: center;
}

.doctor-select {
  margin-top: 10px;
  width: 100%;
  padding: 5px;
}

.button-group {
  margin-top: 20px;
}

.cancel-button,
.confirm-button {
  padding: 5px 10px;
  border-radius: 5px;
  cursor: pointer;
}

.cancel-button {
  background-color: #ccc;
  margin-right: 10px;
}

.confirm-button {
  background-color: #007bff;
  color: white;
}
</style>
