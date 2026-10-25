// MIT licensed; project license in ../LICENSE, upstream in lzokay/LICENSE.
#include "lzokay/lzokay.hpp"
#include <cstring>
#include <vector>
#include <limits>

#ifdef _WIN32
#define NULLPHAAZE_CALL __cdecl
#else
#define NULLPHAAZE_CALL
#endif

// A small C ABI for the Python ctypes caller. Compression uses a worst-case scratch
// buffer so even short caller buffers cannot overrun inside the upstream codec.
extern "C" int NULLPHAAZE_CALL compress_without_dict(const uint8_t* src, int src_size,
    uint8_t* dst, int capacity, int* written) noexcept {
  if (!written) return -1;
  *written = 0;
  if (!src || !dst || src_size < 0 || capacity < 0) return -1;
  try {
    std::vector<uint8_t> buffer(lzokay::compress_worst_size(src_size));
    std::size_t size = 0;
    auto result = lzokay::compress(src, src_size, buffer.data(), buffer.size(), size);
    if (result != lzokay::EResult::Success) return static_cast<int>(result);
    if (size > static_cast<std::size_t>(capacity)) return -3;
    std::memcpy(dst, buffer.data(), size);
    *written = static_cast<int>(size);
    return 0;
  } catch (...) { return -1; }
}

extern "C" int NULLPHAAZE_CALL decompress(const uint8_t* src, int src_size,
    uint8_t* dst, int capacity, int* written) noexcept {
  if (!written) return -1;
  *written = 0;
  if (!src || !dst || src_size < 0 || capacity < 0) return -1;
  std::size_t size = 0;
  auto result = lzokay::decompress(src, src_size, dst, capacity, size);
  if (result != lzokay::EResult::Success) return static_cast<int>(result);
  if (size > static_cast<std::size_t>(capacity)) return -3;
  *written = static_cast<int>(size);
  return 0;
}
