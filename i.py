import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import io


class MyHandler(FileSystemEventHandler):
    def on_moved(self, event):
        print("on_moved")
        print(event.src_path)
        """Called when a file or a directory is moved or renamed.

        :param event:
            Event representing file/directory movement.
        :type event:
            :class:`DirMovedEvent` or :class:`FileMovedEvent`
        """

    def on_created(self, event):
        print("on_creeated")
        print(event.src_path)
        """Called when a file or directory is created.

        :param event:
            Event representing file/directory creation.
        :type event:
            :class:`DirCreatedEvent` or :class:`FileCreatedEvent`
        """

    def on_deleted(self, event):
        print("on_deleted")
        print(event.src_path)
        """Called when a file or directory is deleted.

        :param event:
            Event representing file/directory deletion.
        :type event:
            :class:`DirDeletedEvent` or :class:`FileDeletedEvent`
        """

    def on_modified(self, event):
        print("on_modified")
        print(event.src_path)
        """Called when a file or directory is modified.

        :param event:
            Event representing file/directory modification.
        :type event:
            :class:`DirModifiedEvent` or :class:`FileModifiedEvent`
        """


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    from subprocess import call
    import subprocess

    filename12 = raw_input("Enter file path ")
    filetype = filename12.split(".")[-1]
    

    if filetype == "js":
        call(["node", filename12])

    if filetype == "py":
        cmd = 'python ' + filename12
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, err = p.communicate()
        result = out.split('\n')
        for lin in result:
            if not lin.startswith('#'):
                print(lin)



    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()
