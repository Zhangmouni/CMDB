from .base import SSHandSaltHandler


class SaltHandler(SSHandSaltHandler):

    def cmd(self, command, hostname=None):
        """
        调用saltstack远程连接主机并执行命令（saltstack的master）
        :param hostname:主机名
        :param command: 要执行的命令
        :return:
        """
        import salt.client
        local = salt.client.LocalClient()
        result = local.cmd(hostname, 'cmd.run', [command])
        return result[hostname]

    def handler(self):
        print('salt')
