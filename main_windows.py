import wx
from src.core.md5_utils import calc_string_md5, calc_file_md5
from src.utils.validators import is_valid_mac


class MD5ToolFrame(wx.Frame):
    def __init__(self, parent, title, bg_image_path):
        super().__init__(parent, title=title, size=(600, 400))

        # ===== 颜色配置 =====
        self.bg_color = "#FFC0CB"  # 粉色背景
        self.input_bg = "#90EE90"  # 浅绿色输入框
        self.title_color = "#FFFFE0"  # 淡黄色标题

        # ===== 主布局 =====
        panel = wx.Panel(self)
        panel.SetBackgroundColour(self.bg_color)  # 设置主面板背景色[2,4](@ref)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # ===== 输入控件 =====
        # 标题样式设置
        title_style = wx.StaticText(panel, label="输入内容（MAC地址/任意字符）:")
        title_style.SetForegroundColour(self.title_color)  # 标题文字颜色[8](@ref)

        # 输入框样式设置
        self.input_ctrl = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER)
        self.input_ctrl.SetBackgroundColour(self.input_bg)  # 输入框背景色[1,4](@ref)

        # 文件选择器文本部分颜色设置
        self.file_picker = wx.FilePickerCtrl(panel)
        self.file_picker.GetTextCtrl().SetBackgroundColour(self.input_bg)  # 文件路径输入框[1](@ref)

        # 结果框样式
        self.result_ctrl = wx.TextCtrl(panel, style=wx.TE_READONLY)
        self.result_ctrl.SetBackgroundColour(self.input_bg)  # 结果框背景色[4](@ref)

        # ===== 按钮样式 =====
        btn_calc_str = wx.Button(panel, label="计算字符串MD5")
        btn_calc_file = wx.Button(panel, label="计算文件MD5")
        btn_calc_str.Bind(wx.EVT_BUTTON, self.on_calc_string)
        btn_calc_file.Bind(wx.EVT_BUTTON, self.on_calc_file)

        # ===== 布局管理 =====
        # 添加带颜色的标题组件
        vbox.Add(title_style, 0, wx.ALL, 5)
        vbox.Add(self.input_ctrl, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(btn_calc_str, 0, wx.ALL, 5)

        # 文件选择器标题
        file_title = wx.StaticText(panel, label="或选择文件:")
        file_title.SetForegroundColour(self.title_color)  # 文件选择标题[8](@ref)
        vbox.Add(file_title, 0, wx.ALL, 5)

        vbox.Add(self.file_picker, 0, wx.EXPAND | wx.ALL, 5)
        vbox.Add(btn_calc_file, 0, wx.ALL, 5)

        # 结果标题
        result_title = wx.StaticText(panel, label="MD5结果:")
        result_title.SetForegroundColour(self.title_color)  # 结果标题[8](@ref)
        vbox.Add(result_title, 0, wx.ALL, 5)

        vbox.Add(self.result_ctrl, 0, wx.EXPAND | wx.ALL, 5)
        panel.SetSizer(vbox)

    def on_paint(self, event):
        """绘制背景图片"""
        dc = wx.PaintDC(self)
        dc.DrawBitmap(self.bg_image, 0, 0, True)

    def on_calc_string(self, event):
        input_str = self.input_ctrl.GetValue()
        if is_valid_mac(input_str):
            self.result_ctrl.SetValue(calc_string_md5(input_str))
        else:
            wx.MessageBox("非标准MAC地址格式，将按普通字符串计算", "提示")
            self.result_ctrl.SetValue(calc_string_md5(input_str))

    def on_calc_file(self, event):
        file_path = self.file_picker.GetPath()
        if file_path:
            self.result_ctrl.SetValue(calc_file_md5(file_path))


if __name__ == "__main__":
    app = wx.App()
    frame = MD5ToolFrame(None, "MD5计算工具", "src/gui/resources/bg.png")  # 替换实际背景图路径
    frame.Show()
    app.MainLoop()
