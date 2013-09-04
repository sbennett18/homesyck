def basename(name, suffix=''):  # {
    if suffix and name.endswith(suffix):
        return name[:-len(suffix)]
    return name
# }


class Pathname(object):  # {
    def __init__(self, path):
       self._path = path
       self.dirname = os.path.dirname(path)
       self.directory = os.path.isdir(path)
       self.expand_path = os.path.abspath(path)
# }


def git_clone(repo, config = {}):  # {
    destination = config.get('destination', None) or Pathname(basename(repo, '.git'))

    destination = Pathname.new(destination) unless destination.kind_of?(Pathname)
    FileUtils.mkdir_p destination.dirname

    if ! destination.directory?
        say_status 'git clone', "#{repo} to #{destination.expand_path}", :green unless options[:quiet]
        system "git clone -q --recursive #{repo} #{destination}" unless options[:pretend]
    else
        say_status :exist, destination.expand_path, :blue unless options[:quiet]
# }
