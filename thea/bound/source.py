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
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        self._announce_update()


class BoundComboSelection(BoundValue):

    def __init__(self, items, selected_item):
        super(BoundComboSelection, self).__init__(items)
        self.__set_selected_item(selected_item)

    @property
    def selected_item(self):
        return self.__selected_item

    @selected_item.setter
    def selected_item(self, item):
        self.__set_selected_item(item)
        self._announce_update()

    def __set_selected_item(self, item):
        if item in self._value:
            self.__selected_item = item
        else:
            raise LookupError('Unable to find item: {0} in selection'.format(item))