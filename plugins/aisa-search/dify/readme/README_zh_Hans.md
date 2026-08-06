# AIsa Search

AIsa Search 为 Dify 提供五个只读搜索工具：网页搜索、网页内容提取、
X/Twitter 搜索、YouTube 搜索和学术文献搜索。工具返回带来源链接的结构化
JSON，可供 Agent 和 Workflow 使用。

## 配置

从 <https://console.aisa.one> 获取 AIsa API Key。安装插件后，在 Dify 的
Provider 凭据界面输入密钥。密钥只作为 Bearer 凭据发送到
`https://api.aisa.one`，不会包含在工具输出中。

## 工具

- **网页搜索**：搜索公开网页和最新来源。
- **网页提取**：提取一至三个公开 HTTP(S) URL 的内容。
- **X/Twitter 搜索**：通过高级查询搜索公开帖子。
- **YouTube 搜索**：搜索相关视频和频道。
- **学术搜索**：搜索论文与学术证据。

网页提取工具会拒绝内网地址、本地地址、带凭据的 URL，以及非 HTTP(S)
URL。单个响应最大为 5 MiB。
