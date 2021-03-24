# SE104.L23
🚀 This is a project for [SE104.L23]Software engineering (University of Information Technology VNU-HCM)

## Members
1. 19521225 - Văn Viết Hiếu Anh
2. 19522206 - Nguyễn Đức Thắng
3. 19521848 - Nguyễn Xuân Minh
4. 19522054 - Lê Văn Phước
5. 19521958 - Văn Viết Nhật

## Ideas

1. 📚 Book Finder App
2. 📷 Image viewer
3. ✅ To-do list
4. 📝 Note app with Markdown
5. 👻 Some scrapping data app like VNExpress Desktop

## Architecture

Hiểu đơn giản là tách server và client side ra riêng. Khi sử dụng thì người dùng sẽ gửi yêu cầu lên server để server xử lý với database hoặc tính toán sau đó trả về kết quả.

Mình sẽ xây dựng 2 lớp đơn giản như trên thôi. Server tạo router cho API còn client side là phần ở trên máy sẽ có giao diện, display, xử lý task đơn giản và gửi request.

👍**Hay** 

1. Vì chia 2 phía nên kiến trúc này có thể dễ dàng phát triển 2 phía độc lập
2. Dễ dàng mở rộng vì nếu muốn thêm một tập hợp chức năng thì chỉ cần tạo thêm 1 RESTful API server mới
3. Dễ dàng tạo nhiều app khác nhau ở phía client server (mobile, web app, desktop app)
4. App làm ra bao luôn chức năng đồng bộ bằng cloud

👎**Dỡ**

1. Cái này thực sự hơi khó cần biết công nghệ làm server
2. Team phải biết dùng tool 1 chút mới dễ làm (tool dễ dùng lắm)
3. Phải phát triển chức năng kiểu real-time (khó lắm, nhưng trường hợp app mình làm cần thôi) hoặc yêu cầu luôn là phải có mạng mới xài app được.

## Technology

#### App

**1.**[Electron](https://www.electronjs.org/)

VS Code, Discord, Notion, Twitch, Microsoft Team, Figma (thực ra cũng đừng đánh giá cao quá tại vì big tech thì có trick để app chạy nhanh)

- Ngôn ngữ: JS, html, css (sass, less, scss)
- Hay
  1. Thiết kế giao diện cực kỳ nhanh + nhẹ + dễ + đẹp
  2. Phát triển theo hướng Client-server cực kì dễ vì axios khá dễ dùng
  3. Cross-platforms
  4. Dễ học đủ để làm được nếu ae chưa có kinh nghiệm + tutorial khá nhiều vì cộng đồng lớn
- Dỡ
  1. Nó được đánh giá là chạy hơi chậm so với các công nghệ khác (nếu tác vụ xử lý nặng)
  2. Có một số tín năng trên các hệ điều hành có thể không tận dụng được vì không phải native mà dựa vào chromium để chạy
  3. Hybrid

#### Server
**1. Django**

- Ngôn ngữ: Python
- Hay
  1. Làm mọi thứ cực kì nhanh, mì ăn liền chính hiệu 🍜
  2. Có sẵn CRM, không cần làm vẫn có ăn
  3. Python thì bắt buộc học cả khoa nhé :)
  4. Dễ học
- Dỡ
  1. Deploy hơi khó
  2. Khó ở với document-oriented database program (MongoDB)

```python
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    post = models.CharField('Post', max_length=280)
    post_date = models.DateTimeField("Post date", auto_now_add=True)

    class Meta:
        verbose_name = ("post")
        verbose_name_plural = ("posts")

        ordering = ['-post_date']

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
```
