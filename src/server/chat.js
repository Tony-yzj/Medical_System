const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
app.use(bodyParser.json());
app.use(cors({ origin: 'http://localhost:8080' }));

app.post('/ask', (req, res) => {
  const { question } = req.body;

  // Process the question and generate a response
  const response = processQuestion(question);

  // Simulate a delay to mimic server processing time
  setTimeout(() => {
    res.json({ response });
  }, 1000);
});

function processQuestion(question) {
  // Here, you can implement your logic to process the question and generate an appropriate response.
  // You can use any NLP or AI libraries/tools for natural language processing and question answering.

  // For example, a simple hardcoded response
  if (question.toLowerCase().includes('你好') || question.toLowerCase().includes('您好')) {
    return '您好，这里是校医院的门诊预约系统，请问我有什么可以帮您的吗?';
  }
  else if (question.toLowerCase().includes('肚子疼') || question.toLowerCase().includes('腹痛')) {
    return '您可以去消化内科或者普内科就诊，他们是专门处理肚子疼的科室。';
  } else if (question.toLowerCase().includes('流感') || question.toLowerCase().includes('感冒')) {
      return '建议您去感染科，他们是专门处理感染病的科室。';
  } else if (question.toLowerCase().includes('哮喘') || question.toLowerCase().includes('呼吸困难')) {
      return '建议您去呼吸内科，他们是专门处理呼吸系统疾病的科室。';
  } else if (question.toLowerCase().includes('手臂肿') || question.toLowerCase().includes('骨折')) {
      return '您可以选择去骨科或者外科就诊。';
  }
  else if (question.toLowerCase().includes('头痛') || question.toLowerCase().includes('失眠')) {
      return '您可以去神经内科就诊，他们是专门处理神经系统疾病的科室。';
  } else if (question.toLowerCase().includes('皮肤') || question.toLowerCase().includes('疹子') || question.toLowerCase().includes('过敏')) {
      return '建议您去皮肤科就诊，他们是专门处理皮肤疾病的科室。';
  } else if (question.toLowerCase().includes('眼睛') || question.toLowerCase().includes('模糊')) {
      return '建议您去眼科就诊，他们是专门处理眼部疾病的科室。';
  } else if (question.toLowerCase().includes('耳鸣') || question.toLowerCase().includes('听不清楚')) {
      return '您可以选择去耳鼻喉科就诊。';
  } 
  else if (question.toLowerCase().includes('谢谢') || question.toLowerCase().includes('感谢')) {
    return '不客气呢！很高兴为您服务~';
  } 
  else {
      return "我不太清楚您的问题，请问还有其他问题吗？";
  }
}

const PORT = 8001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

// server.js

// server.js

// const express = require('express');
// const bodyParser = require('body-parser');
// const axios = require('axios');
// const cors = require('cors');

// const app = express();
// const port = 8001;

// var config={
// 	key:"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",//API key token or Secret-API-key
// 	engine : "davinci"
// };

// // 解析请求体
// app.use(bodyParser.json());
// app.use(cors({ origin: 'http://localhost:8080' }));

// app.post('/ask',(req,res)=>{


//   (async ()=>{
//   try{
//     const message=req.body.message;//请求消息体的文本消息内容
    
    
//   const api_url='https://api.openai.com/v1/engine/'+config.engine+'/completions';
  
//   var headers={
//    'Content-Type': 'application/json',
//    auth:`Bearer ${config.key}`
//   };
  
//     console.log(req.body)
//           const prompt=[message] +"   ";  // Initial seed
      
//     const data= {
//             prompt: prompt,
//             max_tokens: 300,
//                 temperature:0.8,n :1 ,presence_penalty :0,delay :false }
//         let res = await fetch(api_url,{method:'POST',headers,body: JSON.stringify(data)})
//           .then(response => response.json())
//       //         if(!('choices' in res)){
//       // console.error("Error calling GPT API",res);
//       //        throw new Error("Create Session Token request failed");
//       //          }
//             res.status(200).json({ message:(res.choices[0].text)});
  
//        }catch(e){
//          console.log(e);
  
//         }
  
//   })()
  
//   });

// // 启动服务器
// app.listen(port, () => {
//   console.log(`Server is running on http://localhost:${port}`);
// });

