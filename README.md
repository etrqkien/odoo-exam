# odoo-exam
## Bài test số 1  

Tạo branch với tên branch là tên của mình. Thực hiện viết câu trả lời trực tiếp vào file này hoặc viết code khi có yêu cầu.  

### Câu 1:  
Tạo file odoo-exam.conf chứa các config tối thiểu để có thể chạy được odoo  
Viết lệnh với odoo-bin sử dụng file config trên để chạy odoo  
Viết lệnh với odoo-bin sử dụng file config trên để update module project, tên database sử dụng là test-project  
Muốn chạy odoo ở cổng 69 thì phải làm thế nào. Hãy viết cả 2 cách: chỉ định cổng ở dòng lệnh với odoo-bin và chỉ định cổng trong file config.  

Trả lời:  
+ -c ../myaddons/odoo.conf -d test-project -u odoo-exam 
+ ..\myaddon\odoo.conf -d test-project -u odoo-exam --xmlrpc-port 69

### Câu 2:  
Tạo module project-base : (Viết lệnh tạo module bằng scaffold)  
- có model exam.project gồm các trường:   
_+ name: tên project   
_+ manager_user_id : id user quản lý   
_+ start_date : ngày bắt đầu dự án   
_+ due_date : ngày kết thúc dự án   
_+ task_ids : danh sách task của dự án  
- có model exam.task gồm các trường:   
_+ name : tên task   
_+ user_id : id user thực hiện task   
_+ start date: ngày giờ bắt đầu task   
_+ due_date : ngày giờ kết thúc task   
_+ project_id : id của project  
- Tạo menu Project để hiển thị danh sách project mặc định hiển thị dạng kanban với trường name, start date, end date.  
- Tạo các view cơ bản (tree, form) cho 2 model trên. Hiển thị toàn bộ các trường có ở 2 model này.  
- Riêng form view của exam.project yêu cầu hiển thị danh sách các task của project ở dạng kanban với trường name  
- Tạo dữ liệu demo cho User, Project, Task. Mỗi model khoảng 3 đến 5 bản ghi demo (dữ liệu demo tự chọn)

Chú ý: user sử dụng bảng res_users của hệ thống. Hãy tự depend tới module cần thiết để có thể sử dụng được model res_users.  

Trả lời:  
( ... lệnh tạo module bằng scaffold ... )  
++ python3 odoo-bin scaffold myproject myaddons
### Câu 3:  
Tạo module project-extern chứa các mở rộng:  
- exam.project: thêm trường status kiểu selection : init, finish, fail . Mặc định init . Danh sách project mặc định filter chỉ hiện các project init (thêm filter init) . Hiển thị trường này ra form view của project.  
- exam.project: thêm trường compute : working_status kiểu selection: chưa bắt đầu, đang hoạt động, đã kết thúc . Giá trị tính như sau: nếu ngày hiện tại < start_date thì giá trị trường này là chưa bắt đầu. Nếu star date < ngày hiện tại < end date thì giá trị trường này là đang hoạt động. Còn lại nếu end date < ngày hiện tại thì giá trị trường này là đã kết thúc. Hiển thị trường này ra form view  
- exam.task: thêm trường status: kiểu selection: init, inprogress, finish . Hiện trường này ra form view  
- exam.task : thêm trường compute working_status: kiểu selection: not start, in working time, finish, over dead line. Giá trị tính như sau:   
_+ Nếu status là finish thì working_status là finish   
_+ Nếu ngày hiện tại < start date thì working_status là not start   
_+ Nếu start date < ngày hiện tại < end date thì working_status là in working time   
_+ Nếu end date < ngày hiện tại thì working_status là: over dead line Hiển thị trường này ra form view.
