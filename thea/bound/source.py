class BoundSource(object):

    def __init__(self):
        self.__subscribers = set()

    def subscribe(self, subscriber):
        """
        Subscribes a BoundTarget to the BoundSource. The BoundTarget will then be updated whenever the BoundSource
        changes.

        :param subscriber: A bound target.
        """
        self.__subscribers.add(subscriber)

    def _announce_update(self):
        for subscriber in self.__subscribers:
            subscriber.update_bound_target(self)


class BoundValue(BoundSource):

    def __init__(self, value):
        super(BoundValue, self).__init__()
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value
        self._announce_update()


class BoundListSelection(BoundSource):

    def __init__(self, items, selected_item=None):
        super(BoundListSelection, self).__init__()

        self.__items = items
        self.__set_selected_item(selected_item)

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, new_items):
        self.__items = new_items
        self.__set_selected_item(None)
        self._announce_update()

    @property
    def selected_item(self):
        return self.__selected_item

    @selected_item.setter
    def selected_item(self, item):
        self.__set_selected_item(item)
        self._announce_update()

    @property
    def current_index(self):
        if self.__selected_item:
            return self.__items.index(self.__selected_item)
        return 0

    def __set_selected_item(self, item):
        if not item:
            self.__selected_item = None
        elif item in self.__items:
            self.__selected_item = item
        else:
            raise LookupError('Unable to find item: {0} in selection'.format(item))