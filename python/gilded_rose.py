# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class QualityUpdater:
    def update(self, item: Item):
        raise NotImplementedError

    @staticmethod
    def increase_quality(item: Item, amount: int = 1):
        item.quality = min(item.quality + amount, 50)

    @staticmethod
    def decrease_quality(item: Item, amount: int = 1):
        item.quality = max(item.quality - amount, 0)

    @staticmethod
    def decrement_sell_in(item: Item):
        item.sell_in -= 1


class NormalUpdater(QualityUpdater):
    def update(self, item: Item):
        self.decrease_quality(item, 1)
        self.decrement_sell_in(item)
        if item.sell_in < 0:
            self.decrease_quality(item, 1)


class ConjuredUpdater(NormalUpdater):
    def update(self, item: Item):
        self.decrease_quality(item, 2)
        self.decrement_sell_in(item)
        if item.sell_in < 0:
            self.decrease_quality(item, 2)


class AgedBrieUpdater(QualityUpdater):
    def update(self, item: Item):
        self.increase_quality(item, 1)
        self.decrement_sell_in(item)
        if item.sell_in < 0:
            self.increase_quality(item, 1)


class BackstageUpdater(QualityUpdater):
    def update(self, item: Item):
        self.increase_quality(item, 1)
        if item.sell_in < 11:
            self.increase_quality(item, 1)
        if item.sell_in < 6:
            self.increase_quality(item, 1)
        self.decrement_sell_in(item)
        if item.sell_in < 0:
            item.quality = 0


class SulfurasUpdater(QualityUpdater):
    def update(self, item: Item):
        pass


class GildedRose(object):
    UPDATERS = [
        ("Sulfuras, Hand of Ragnaros", SulfurasUpdater()),
        ("Aged Brie", AgedBrieUpdater()),
        ("Backstage passes to a TAFKAL80ETC concert", BackstageUpdater()),
        ("conjured", ConjuredUpdater()),
    ]

    def __init__(self, items):
        self.items = items

    def updater_for(self, item: Item):
        name_lower = item.name.lower()
        for key, updater in self.UPDATERS:
            if key.lower() == "conjured":
                if name_lower.startswith("conjured"):
                    return updater
                continue
            if item.name == key:
                return updater
        return NormalUpdater()

    def update_quality(self):
        for item in self.items:
            self.updater_for(item).update(item)

