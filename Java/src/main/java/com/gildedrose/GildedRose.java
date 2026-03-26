package com.gildedrose;

class GildedRose {
    Item[] items;

    public GildedRose(Item[] items) {
        this.items = items;
    }

    public void updateQuality() {
        for (Item item : items) {
            updateItem(item);
        }
    }

    private void updateItem(Item item) {
        if (item.name.equals("Aged Brie")) {
            updateAgedBrie(item);
        } else if (item.name.equals("Backstage passes to a TAFKAL80ETC concert")) {
            updateBackstagePasses(item);
        } else if (item.name.equals("Sulfuras, Hand of Ragnaros")) {
            // Sulfuras does not change
        } else {
            updateNormalItem(item);
        }

        if (!item.name.equals("Sulfuras, Hand of Ragnaros")) {
            item.sellIn--;
        }

        if (item.sellIn < 0) {
            updateExpiredItem(item);
        }
    }

    private void updateNormalItem(Item item) {
        if (item.quality > 0) {
            item.quality--;
        }
    }

    private void updateAgedBrie(Item item) {
        if (item.quality < 50) {
            item.quality++;
        }
        if (item.sellIn < 0 && item.quality < 50) {
            item.quality++;
        }
    }

    private void updateBackstagePasses(Item item) {
        if (item.quality < 50) {
            item.quality++;
            if (item.sellIn < 11 && item.quality < 50) {
                item.quality++;
            }
            if (item.sellIn < 6 && item.quality < 50) {
                item.quality++;
            }
        }
        if (item.sellIn < 0) {
            item.quality = 0;
        }
    }

    private void updateExpiredItem(Item item) {
        if (item.name.equals("Aged Brie")) {
            if (item.quality < 50) {
                item.quality++;
            }
        } else if (item.name.equals("Backstage passes to a TAFKAL80ETC concert")) {
            item.quality = 0;
        } else if (!item.name.equals("Sulfuras, Hand of Ragnaros")) {
            if (item.quality > 0) {
                item.quality--;
            }
        }
    }
}
