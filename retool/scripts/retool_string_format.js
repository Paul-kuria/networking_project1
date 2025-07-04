var currentCell = "2025-05-31T08:10:52.00Z"(() => {
  const [datePart, timePart] = currentCell.split("T");
  const isoString =
    "${datePart}T${timePart.slice(0,2)}:${timePart.slice(2,4)}${timePart.slice(4,6)}Z";
  const dateObj = new Date(isoString);
  dateObj.setHours(dateObj.getHours() + 3);
  return dateObj.toISOString().replace("T", " ").replace(".000Z", "");
});

// Simple conversion if already in isoformat, to eat timezone
{
  {
    (() => {
      const dateObj = new Date(item);
      dateObj.setHours(dateObj.getHours() + 3);
      return dateObj.toISOString();
    })();
  }
}
