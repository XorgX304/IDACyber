from PyQt5.QtGui import qRgb
from idacyber import ColorFilter
from ida_bytes import get_item_size
from ida_kernwin import register_timer, unregister_timer, warning
import winsound

# made with Piskel (https://www.piskelapp.com/)
hubert = [
[
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xffb38150, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff9f7245, 0xffb8895b, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0xff000000, 0xff755433, 0xff623c16, 0xff623c16, 0xff623c16, 0xffbc9065, 0xffb38150, 0xff623c16, 0xff623c16, 0xff623c16, 0xffb38150, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff00ade0, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00ade0, 0xff755433, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xff000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff60452a, 0xff8a633c, 0xffbc9065, 0xffb38150, 0xff9f7245, 0xff60452a, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff60452a, 0xff9f7245, 0xffb38150, 0xffb38150, 0xffb38150, 0xff755433, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff9f7245, 0xff805b38, 0xff000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff755433, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff60452a, 0xff8a633c, 0xff755433, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000
],
[
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffbc9065, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xffb38150, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff9f7245, 0xffb8895b, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xffb38150, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff9f7245, 0xffb8895b, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0xff000000, 0xff755433, 0xff623c16, 0xff623c16, 0xff623c16, 0xffbc9065, 0xffb38150, 0xff623c16, 0xff623c16, 0xff623c16, 0xffb38150, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 
0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xff000000, 
0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff60452a, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff755433, 0xffb38150, 0xffbc9065, 0xff9f7245, 0xff9f7245, 0xff805b38, 0xff000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff755433, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff60452a, 0xff8a633c, 0xff755433, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000
],
[
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffbc9065, 0xffb38150, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0xff000000, 0xff755433, 0xff623c16, 0xff623c16, 0xff623c16, 0xffbc9065, 0xffb38150, 0xff623c16, 0xff623c16, 0xff623c16, 0xffb38150, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 
0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xff000000, 
0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff60452a, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff755433, 0xffb38150, 0xffbc9065, 0xff9f7245, 0xff9f7245, 0xff805b38, 0xff000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff755433, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff60452a, 0xff8a633c, 0xff755433, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000
],
[
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xffbc9065, 0xffbc9065, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffbc9065, 0xffb8895b, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xffb38150, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xffb38150, 0xffbc9065, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0xff000000, 0xff8a633c, 0xff623c16, 0xff623c16, 0xff623c16, 0xffbc9065, 0xffb38150, 0xff623c16, 0xff623c16, 0xff623c16, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xff000000, 
0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff60452a, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff755433, 0xffb38150, 0xffbc9065, 0xff9f7245, 0xff9f7245, 0xff805b38, 0xff000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff755433, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff60452a, 0xff8a633c, 0xff755433, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000
],
[
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xffb38150, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff9f7245, 0xffb8895b, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xffb38150, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff9f7245, 0xffb8895b, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0xff000000, 0xff755433, 0xff623c16, 0xff623c16, 0xff623c16, 0xffbc9065, 0xffb38150, 0xff623c16, 0xff623c16, 0xff623c16, 0xffb38150, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xff000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff60452a, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff755433, 0xffb38150, 0xffbc9065, 0xff9f7245, 0xff9f7245, 0xff805b38, 0xff000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff755433, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff60452a, 0xff8a633c, 0xff755433, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000
],
[
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xffb38150, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff9f7245, 0xffb8895b, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xffb38150, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff9f7245, 0xffb8895b, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0xff000000, 0xff755433, 0xff623c16, 0xff623c16, 0xff623c16, 0xffbc9065, 0xffb38150, 0xff623c16, 0xff623c16, 0xff623c16, 0xffb38150, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xff000000, 
0x00000000, 0xff000000, 0xff755433, 0xff8a633c, 0xff60452a, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff755433, 0xffb38150, 0xffbc9065, 0xff9f7245, 0xff9f7245, 0xff805b38, 0xff000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff755433, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff60452a, 0xff8a633c, 0xff755433, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000
],
[
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff623c16, 0xff623c16, 0xff623c16, 0xffbc9065, 0xffb38150, 0xff623c16, 0xff623c16, 0xff623c16, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xff9f7245, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff00ade0, 0xff8a633c, 0xffbc9065, 0xffb38150, 0xff9f7245, 0xff00ade0, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff60452a, 0xff9f7245, 0xffb38150, 0xffb38150, 0xffb38150, 0xff60452a, 0xffb38150, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff60452a, 0xff9f7245, 0xffb38150, 0xffb38150, 0xffb38150, 0xff755433, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff805b38, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff755433, 0xff8a633c, 0xff755433, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000
],
[
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xffb38150, 0xff9f7245, 0xff8a633c, 0xff8a633c, 0xff9f7245, 0xffb8895b, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff623c16, 0xff623c16, 0xffbc9065, 0xffb38150, 0xff623c16, 0xff623c16, 0xff623c16, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff00c5ff, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff00ade0, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00ade0, 0xff755433, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff60452a, 0xff8a633c, 0xffbc9065, 0xffb38150, 0xff9f7245, 0xff60452a, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xff9f7245, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff60452a, 0xff9f7245, 0xffb38150, 0xffb38150, 0xffb38150, 0xff755433, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff805b38, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff60452a, 0xff8a633c, 0xff755433, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000
],
[
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffc59f7a, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff623c16, 0xff623c16, 0xff623c16, 0xffbc9065, 0xffb38150, 0xff623c16, 0xff623c16, 0xff623c16, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xff9f7245, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff00ade0, 0xff8a633c, 0xffbc9065, 0xffb38150, 0xff9f7245, 0xff00ade0, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff60452a, 0xff9f7245, 0xffb38150, 0xffb38150, 0xffb38150, 0xff60452a, 0xffb38150, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff60452a, 0xff9f7245, 0xffb38150, 0xffb38150, 0xffb38150, 0xff755433, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff805b38, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff755433, 0xff8a633c, 0xff755433, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000
],
[
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xffb38150, 0xff9f7245, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffb38150, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffc59f7a, 0xffc59f7a, 0xffbc9065, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff623c16, 0xff623c16, 0xff623c16, 0xffbc9065, 0xffb38150, 0xff623c16, 0xff623c16, 0xff623c16, 0xffb38150, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xff9f7245, 0xffb38150, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xffbc9065, 0xffb38150, 0xff8a633c, 0xff00c5ff, 0xff755433, 0xff9f7245, 0xffbc9065, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff00ade0, 0xff8a633c, 0xffbc9065, 0xffb38150, 0xff9f7245, 0xff00ade0, 0xff9f7245, 0xffbc9065, 0xffbc9065, 0xffb38150, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff60452a, 0xff9f7245, 0xffb38150, 0xffb38150, 0xffb38150, 0xff60452a, 0xffb38150, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff60452a, 0xff9f7245, 0xffb38150, 0xffb38150, 0xffb38150, 0xff755433, 0xffb38150, 0xffb38150, 0xff9f7245, 0xff805b38, 0xff000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff755433, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff9f7245, 0xff9f7245, 0xff8a633c, 0xff000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff8a633c, 0xff755433, 0xff8a633c, 0xff755433, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0xff000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 
0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000
]
]

class Hubert(ColorFilter):
    name = "Hubert"
    help =  "Hubert"
    highlight_cursor = False
    width = 16
    lock_width = True
    sync = False
    lock_sync = True
    show_address_range = False
    zoom = 8
    link_pixel = False

    def __init__(self, pw):
        self.pw = pw
        self.idx_frame = 0
        self.timer = None
        self.jump_fw = True
        return

    def _timer_cb(self):
        global hubert

        if self.pw:
            self.idx_frame = (self.idx_frame+1) % len(hubert)
            self.pw.on_filter_request_update()
        return 1000/12

    def on_activate(self, idx):
        if self.timer is not None:
            unregister_timer(self.timer)
        self.timer = register_timer(200, self._timer_cb)
        return

    def on_deactivate(self):
        if self.timer is not None:
            unregister_timer(self.timer)
            self.timer = None
        return       

    def on_process_buffer(self, buffers, addr, size, mouse_offs):
        global hubert

        colors = []
        framesize = len(hubert[0])

        start_offs = (size/2) - (framesize/2)
        start_offs -= (start_offs%Hubert.width)

        # black bg
        for i in xrange(start_offs):
        	colors.append((False, 0))

        # hubert
        frame = hubert[self.idx_frame]
        for color in frame:
            colors.append((True, color))

        # black bg
        for i in xrange(start_offs + framesize):
        	colors.append((False, 0))

        return colors


def FILTER_INIT(pw):
    return Hubert(pw)
    
def FILTER_EXIT():
    return