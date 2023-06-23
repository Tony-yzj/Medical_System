// 引入所需的依赖项
const { mount } = require('@vue/test-utils');
const { JSDOM } = require('jsdom');

// 使用jsdom模拟浏览器环境
const { window } = new JSDOM('<!doctype html><html><body></body></html>');
global.window = window;
global.document = window.document;
global.navigator = {
  userAgent: 'node.js',
};

// 引入要测试的组件
const Login = require('../src/views/Login.vue').default;

describe('Login.vue', () => {
  it('renders login form correctly', () => {
    // 创建一个Vue实例，并挂载组件
    const wrapper = mount(Login);

    // 断言组件的某些元素是否存在
    expect(wrapper.find('.login-container').exists()).toBe(true);
    expect(wrapper.find('.login-box').exists()).toBe(true);
    expect(wrapper.find('h1').exists()).toBe(true);
    expect(wrapper.find('el-form').exists()).toBe(true);
    expect(wrapper.find('el-input').exists()).toBe(true);
    expect(wrapper.find('el-button').exists()).toBe(true);
    expect(wrapper.find('el-dialog').exists()).toBe(true);
  });
});
