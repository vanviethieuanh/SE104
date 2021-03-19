# SE104.L23
🚀 This is a project for [SE104.L23]Software engineering (University of Information Technology VNU-HCM)

## Members
1. 19521225 - Văn Viết Hiếu Anh
2. 19522206 - Nguyễn Đức Thắng
3. 19521848 - Nguyễn Xuân Minh
4. 19522054 - Lê Văn Phước
5. 19521958 - Văn Viết Nhật
## Architecture

#### 1. [Client-Server](https://en.wikipedia.org/wiki/Client%E2%80%93server_model) ([REST](https://www.youtube.com/watch?v=-MTSQjw5DrM&ab_channel=Fireship), 2 tier)

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

#### 2. [Monolithic](https://en.wikipedia.org/wiki/Monolithic_application) (single-tiered)

📌 Lưu ý ở đây nói về monolithic trong ngữ cảnh hiện tại đơn giản nghĩa là không sử dụng server

Tất cả dồn một chổ và mọi việc đều xử lý trên máy tính của người dùng. Giao diện và xử lý đều do máy người dùng chịu tải. Đa phần ⚙config của hay data của app đều lưu trên local (nếu chơi đúng chuẩn cổ điển, tất nhiên có thể phối hợp với mô hình trên).

👍**Hay** 

1. Vì chơi kiểu cổ điển nên cấu trúc không có gì khác mấy so với mấy cái *app console tính tổng* ngoài phần có bản mặt đẹp hơn
2. Không cần nhùng nhằng server, vì lưu local nên không cần mạng vẫn chạy như bth
3. Đa phần công nghệ tốt trong việc phát triển theo kiến trúc này có thể dễ dàng tận dụng được hết điểm mạnh của hệ điều hành + phần cứng.

👎**Dỡ**

1. Không có khả năng đồng bộ.
2. Team phải biết phối hợp nhịp nhàng + chia module chuẩn thì code mới dễ.

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

**2. WPF**

Tui không tìm đc app nào cả :<

- Ngôn ngữ: C#, XAML
- Hay
  1. Thiết kế giao diện cực kỳ đẹp
  2. Tận dụng được hết chức năng của windows
  3. C# mạnh, cực mạnh (nhưng để nó mạnh mình cũng phải try-hard)
- Dỡ
  1. Theo tôi biết thì đây là dead game của Microsoft (nếu ae search *wpf application* trên google và xem ở *people also ask* sẽ thấy)
  2. xaml cực kì khó và hardcore để xài tốt
  3. Để master C# cũng cần khá nhiều thời gian (kinh nghiệm 1 người dùng 3+ năm)
  4. Tin tôi đi là XAML chạy nặng lắm
  5. Chỉ chạy được trên Windows
  6. Phải mang theo nguyên bộ đồ của Visual Studio

**3. Qt, NodeBox, PyGTK**

Không biết gì nên không nói.

Nếu ae thích ngôn ngữ lập trình nào đó thì tìm như vầy <ngôn ngữ lập trình> + "gui framework"

ví dụ: python gui framework



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

**2. ASP.NET**

Cái này thực chất chưa xài bao giờ nên chỉ tổng hợp báo mạng và kinh nghiệm dùng C# thôi nhé, nếu ae xài rồi thì bổ sung.

- Ngôn ngữ: C#
- Hay
  1. Mạnh, tốc độ thuộc dạng ông bà 🚀 (thực ra thì hệ thống lớn mới thấy rõ khác biệt)
  2. Hàng thuộc big-tech, những doanh nghiệp lâu đời hay dùng
  3. Cấu trúc chuẩn, dễ đọc, dễ chỉnh sữa
  4. Doc đầy đủ từ nhà sản xuất, Microsoft cực kì có tâm, bắt tay dạy từng dòng code
- Dỡ
  1. Nhắc lại để master C# thì khó nhưng nó cũng tương tương C++
  2. C# xưa như trái đất nên code trông khá dài và phải chuẩn chỉ mới ok.
  3. C# thuộc hàng khó dùng, học nhiều mới hiểu được những khái niệm có phần cao siêu của nó.

```Csharp
// Một đoạn code ASP khi làm việc với MongoDB
namespace BooksApi.Models
{
    public class BookstoreDatabaseSettings : IBookstoreDatabaseSettings
    {
        public string BooksCollectionName { get; set; }
        public string ConnectionString { get; set; }
        public string DatabaseName { get; set; }
    }

    public interface IBookstoreDatabaseSettings
    {
        string BooksCollectionName { get; set; }
        string ConnectionString { get; set; }
        string DatabaseName { get; set; }
    }
}
```

**3. NodeJS**

- Ngôn ngữ: JS or Ts
- Hay
  1. Cái này bây giờ cũng thuộc tầm của PHP với ASP rồi, già, nhiều người dùng và mạnh
  2. Doc đầy đủ
  3. Nhiều thư viện hỗ trợ (thuộc dạng top, đa phần thư viện đều mã nguồn mở)
  4. Automation test cực nổi (Jest của Facebook nè, Mocha của cộng đồng phát triển nè)
  5. Xây dựng hệ thống khá nhanh
  6. Có nhiều công cụ hỗ trợ tự động viết code (cũng không dễ xài lắm đâu)
  7. Deploy bằng Docker hay gì cũng cực kì nhanh gọn lẹ
- Dỡ
  1. Nếu chưa học JS bao giờ mà đọc code của mấy thằng viết NodeJS thì đúng là như trên trời rơi xuống, không hiểu gì đâu.
  2. Có nhiều khái niệm mới + hơi khó (Promise, async/await, ...)
  3. CRM trông hơi bần

```javascript
const mongoose = require('mongoose')
const { Schema } = mongoose

const ProductSchema = new Schema(
    {
        title: {
            type: String,
            required: true,
            trim: true,
            unique: true
        },
        type: {
            type: [String],
            required: true,
            trim: true
        },
        price: {
            type: Number,
            required: true,
        },
        hearts: {
            type: Number,
            required: true,
            default: 0,
            min: 0
        }
    }
)
```

#### Database

[Xem video này](https://youtu.be/H3i5X_7muwk)