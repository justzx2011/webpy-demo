#只是玩玩
yum install uwsgi  webpy  

https://github.com/agentzh/ngx_openresty

nginx.conf添加server节点
include /usr/local/openresty/nginx/conf/vhost/xiaofancn.conf;

##xiaofancn.conf
server {
    listen       81; 
    server_name xiaofancn; 
    charset utf-8; 
    location /{#所有的请求都会被路由
        root /home/fansxnet/gitproject/webpy-demo;
        include uwsgi_params;
        uwsgi_pass 127.0.0.1:8000;
        uwsgi_param UWSGI_CHDIR /home/fansxnet/gitproject/webpy-demo;
        uwsgi_param UWSGI_SCRIPT index;
    }
    location /static/ {#单独映射。 
         root /home/fansxnet/gitproject/webpy-demo;
    }
    

 }


##cmd
cd /home/fansxnet/gitproject/webpy-demo/
uwsgi -x uwsgi.xml &
cd /usr/local/openresty
./nginx/sbin/nginx

访问 localhost:81




