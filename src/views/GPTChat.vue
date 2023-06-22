<template>
  <div class="chat-container">
    <div class="chat-messages">
      <!-- 聊天消息 -->
      <div v-for="message in messages" :key="message.id" class="chat-message">
        <div class="message-text">{{ message.text }}</div>
        <div class="message-time">{{ message.time }}</div>
      </div>
    </div>
    <div class="chat-input">
      <!-- 聊天输入框 -->
      <input
        type="text"
        v-model="inputText"
        class="input-field"
        placeholder="输入消息..."
        @keydown.enter="sendMessage"
      />
      <button @click="sendMessage" class="send-button">发送</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      inputText: "",
      messages: [],
    };
  },
  methods: {
    async sendMessage() {
      const message = {
        id: this.messages.length + 1,
        text: this.inputText,
        time: new Date().toLocaleTimeString(),
      };
      this.messages.push(message);
      this.inputText = "";

      // 调用后端接口发送问题并获取回答
      const response = await this.sendQuestion(message.text);
      const answerMessage = {
        id: this.messages.length + 1,
        text: response,
        time: new Date().toLocaleTimeString(),
      };
      this.messages.push(answerMessage);
    },
    async sendQuestion(question) {
      // 向后端发送问题并获取回答
      // 你需要替换以下代码为实际的后端接口调用
      const response = await fetch("http://localhost:8001/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ question }),
      });
      const data = await response.json();
      return data.response;
    },
  },
};
</script>

<style scoped>
.chat-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  padding: 20px;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
}

.chat-message {
  margin-bottom: 10px;
  padding: 10px;
  background-color: #f0f0f0;
  border-radius: 5px;
}

.message-text {
  font-size: 14px;
  color: #333;
}

.message-time {
  font-size: 12px;
  color: #888;
  margin-top: 5px;
}

.chat-input {
  display: flex;
}

.input-field {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.send-button {
    padding: 10px 20px;
    margin-left: 10px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
  
  .send-button:hover {
    background-color: #0056b3;
  }
</style>


