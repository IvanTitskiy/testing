<?php  // add 11.10.2019
    $productsInCart = array();
    $productsInCart2 = array();
    $productsInCartOld = $this->orderdetails['items'];
    foreach ($productsInCartOld as $key => $row) {
        $productsInCart[$key] = $row->category_name;
        $productsInCart2[$key] = $row->product_name;
    }
    //array_multisort($productsInCart, SORT_ASC, $productsInCartOld);
    array_multisort($productsInCart, SORT_ASC, $productsInCart2, SORT_ASC, $productsInCartOld);
	//foreach($this->orderdetails['items'] as $item) {
    foreach($productsInCartOld as $item) {
    //END: add 11.10.2019
		$qtt = $item->product_quantity ;
		$_link = JRoute::_('index.php?option=com_virtuemart&view=productdetails&virtuemart_category_id=' . $item->virtuemart_category_id . '&virtuemart_product_id=' . $item->virtuemart_product_id, FALSE);
		?>
